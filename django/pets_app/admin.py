from django.contrib import admin
from .models import Breed, Pet, VaccinationCard, VetVisit

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ["name", "weight", "height"]

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ["name", "gender"]

@admin.register(VetVisit)
class VetVisitAdmin(admin.ModelAdmin):
    list_display = ["pet", "vet", "date", "notes"]

@admin.register(VaccinationCard)
class VaccinationCardAdmin(admin.ModelAdmin):
    list_display = ["pet", "rabies", "hepatitis"]
