from django.urls import path
from . import views

urlpatterns = [
    path('pets/', views.listPets, name='petsList'),
    path("pets/<str:pet_id>", views.pet, name="pet"),
]