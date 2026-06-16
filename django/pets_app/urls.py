from django.urls import path
from . import views

urlpatterns = [
    path('pets/', views.listPets, name='petsList'),
    path("index/",views.listPets, name="index"),
    path("pets/<str:pet_id>", views.pet, name="pet"),
    path("visit/<str:pet_id>", views.visit, name="visit"),
]