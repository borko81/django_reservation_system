from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from rooms.forms import BedsForm
from rooms.models import BedModel


# Beds
@login_required
def beds_menu(request):
    context = {"title": "Menu"}
    return render(request, template_name="beds/base.html", context=context)


@login_required
def beds_show(request):
    context = {"title": "Show All", "beds": BedModel.objects.all()}
    return render(request, template_name="beds/beds.html", context=context)


@login_required
def bed_create(request):
    form = BedsForm(request.POST or None)

    context = {"title": "Create new", "form": form}

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("rooms:bed")

    return render(request, template_name="beds/bed_create.html", context=context)


@login_required
def bed_edit(request, id):
    bed = get_object_or_404(BedModel, id=id)

    form = BedsForm(request.POST or None, instance=bed or None)

    context = {"title": "Edit", "bed": bed, "form": form}

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("rooms:bed")

    return render(request, template_name="beds/bed_create.html", context=context)


@login_required
def bed_delete(request, id):
    bed = get_object_or_404(BedModel, id=id)
    bed.delete()
    return JsonResponse({"status": "204"})
