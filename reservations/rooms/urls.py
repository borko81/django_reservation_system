from django.urls import path

from . import views, bed_views, type_views, floor_views, rooms_views

app_name = "rooms"
urlpatterns = [
    # Menu 
    path('', views.menu_index, name="menu_index"),
    
    # Floor
    path('flors/', floor_views.floors_show, name="floots"),
    path('floor/create/', floor_views.floor_create, name="floor_create"),
    path('flors/edit/<int:id>/', floor_views.floor_edit, name="floor_edit"),
    path('flors/delete/<int:id>/', floor_views.floor_delete, name="floor_delete"),
    
    # Type
    path("types/", type_views.types_show, name="types"),
    path("type/create/", type_views.type_create, name="type_create"),
    path("types/edit/<int:id>/", type_views.type_edit, name="type_edit"),
    path("types/delete/<int:id>/", type_views.type_delete, name="type_delete"),
    
    # Rooms
    path("rooms/", rooms_views.rooms_show, name="rooms"),
    path("room/create/", rooms_views.room_create, name="room_create"),
    path("room/edit/<int:id>/", rooms_views.room_edit, name="room_edit"),
    path("room/delete/<int:id>/", rooms_views.room_delete, name="room_delete"),
    
    # Bed's
    path("beds/", bed_views.beds_show, name="beds"),
    path("bed/create/", bed_views.bed_create, name="bed_create"),
    path("bed/edit/<int:id>/", bed_views.bed_edit, name="bed_edit"),
    path("bed/delete/<int:id>/", bed_views.bed_delete, name="bed_delete"),
]