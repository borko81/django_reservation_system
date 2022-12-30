from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from rooms import models
from rooms import forms

# Rooms
@login_required
def rooms_menu(request):
    context = {"title": "Menu"}
    return render(request, template_name="rooms/base.html", context=context)


@login_required
def rooms_show(request):
    all_rooms = models.RoomModel.objects.all().order_by("floor_id", "name")
    types = models.RoomTypeModel.objects.all()
    counter = {}
    
    for type in types:
        counter[type] = len(models.RoomTypeModel.objects.get(id=type.id).roommodel_set.all())
    
    context = {"title": "Show All Rooms", "rooms": all_rooms, "counter": counter, "total": len(all_rooms)}
    return render(request, template_name='rooms/rooms.html', context=context)

@login_required
def room_create(request):
    form = forms.RoomForm(request.POST or None)
    context = {"title": "Create New Room", "form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("rooms:room")
    return render(request, template_name='rooms/create_room.html', context=context)

@login_required
def room_edit(request, id):
    room = get_object_or_404(models.RoomModel, id=id)
    form = forms.RoomForm(request.POST or None,  instance=room or None)
    context = {"title": "Edit room", "form": form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("rooms:room")
    return render(request, template_name='rooms/create_room.html', context=context)

@login_required
def room_delete(request, id):
    room = get_object_or_404(models.RoomModel, id=id)
    room.delete()
    return JsonResponse({"status": 204})
