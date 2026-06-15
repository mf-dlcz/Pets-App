from django.http import HttpResponse
from .models import Pet
from django.shortcuts import render

# New view 
def pet(request, pet_id):
    # 1 - prepare application data in a context dict
    context = {"pet": Pet.objects.filter(id=pet_id).first()}

    # 2-3-4 - load template, render it and return the HTTP response
    return render(request, "pets_app/pet.html", context)


def listPets(request):
    context = {
        'pets': Pet.objects.all()
    }

    return render(request, "pets_app/pets.html", context)