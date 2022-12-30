from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rooms import models
from rooms import forms

# Type's
@login_required
def types_menu(request):
    context = {"title": "Menu"}
    return render(request, template_name="types/base.html", context=context)


@login_required
def type_create(request):
    form = forms.RoomTypeForm(request.POST or None)
    context = {"title": "Create new", "form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("rooms:type")
    return render(request, template_name="types/create_type.html", context=context)


@login_required
def types_show(request):
    types = models.RoomTypeModel.objects.all()
    context = {"title": "Show all", "types": types}
    return render(request, template_name="types/types.html", context=context)


@login_required
def type_edit(request, id):
    type = get_object_or_404(models.RoomTypeModel, id=id)
    form = forms.RoomTypeForm(request.POST or None, instance=type or None)
    context = {"title": "Edit type", "form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("rooms:type")

    return render(request, template_name="types/create_type.html", context=context)


@login_required
def type_delete(request, id):
    type = get_object_or_404(models.RoomTypeModel, id=id)
    type.delete()
    return JsonResponse({"status": 204})
