from django.urls import path
from . import views

app_name = "contragent"
urlpatterns = [
    path("", views.menu, name="menu"),
    path("contragents/", views.contragents, name="contragents"),
    path("create/", views.create, name="create"),
    path("edit/<int:id>/", views.edit, name="edit"),
]
