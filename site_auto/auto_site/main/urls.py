from django.contrib import admin
from django.urls import path
from . import views




urlpatterns = [

    path('', views.index, name='home'),
    path('russian_car', views.russian_auto, name='russian_car'),
    path('cars', views.car_list, name='car'),
    path('details', views.details_list, name='details')
]
