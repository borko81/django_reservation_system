from django.urls import path

from . import views


app_name = 'owner'
urlpatterns = [
    path('', views.owner_index, name='owner'),
    path('owner_data/', views.owner_create_update, name='owner_info'),
    path('owner_bank/', views.owner_bank_create_update, name='owner_bank'),
    path('owner_fak_id/', views.owner_fak_id_update, name='owner_fak_id'),
]