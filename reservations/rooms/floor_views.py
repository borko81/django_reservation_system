from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


from . import models
from . import forms

# Floor's
@login_required
def floor_create(request):
    form = forms.FloorForm(request.POST or None)
    context = {"title": "Create new floor", "form": form, "form_create_class": "active"}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("rooms:menu_index")
    return render(request, template_name="floors/floor_create.html", context=context)


@login_required
def floors_show(request):
    floors = models.FloorModel.objects.all()
    context = {"title": "Show all floors", "owner_class": "active", "floors": floors}
    return render(request, template_name="floors/floors_show.html", context=context)


@login_required
def floor_edit(request, id):
    floor = get_object_or_404(models.FloorModel, id=id)
    form = forms.FloorForm(request.POST or None, instance=floor)
    context = {"title": "Edit floor", "form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("rooms:menu_index")
    return render(request, template_name="floors/floor_create.html", context=context)


@login_required
def floor_delete(request, id):
    floor = get_object_or_404(models.FloorModel, id=id)
    floor.delete()
    return JsonResponse({"status": "204"})
