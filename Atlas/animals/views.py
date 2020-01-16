from django.shortcuts import render
from .models import Animal
from . import forms
from . import models


def index(request):
    animals = Animal.objects.all()
    return render(request, 'index.html', {'animals': animals})


def add_animal(request):
    return render(request,'addanimal.html')


def add_animal_form_submission(request):
    form_data=forms.AddAnimal(request.POST)
    if form_data.is_valid():
        Animal=models.Animal()
        Animal.name = form_data.cleaned_data['name']
        Animal.eat = form_data.cleaned_data['eat']
        Animal.environment = form_data.cleaned_data['environment']
        Animal.type = form_data.cleaned_data['type']
        Animal.climate = form_data.cleaned_data['climate']
        Animal.image_url = form_data.cleaned_data['image_url']
        Animal.save()
    context = {
        'formaddanimal':form_data

    }

    return render(request, 'addanimal.html', context)


def SearchView(request):
    animals = Animal.objects.all()
    name_contains_query = request.GET.get('name_contains')
    if name_contains_query !='' and name_contains_query is not None:
        animals = animals.filter(name__icontains = name_contains_query)
    context = {
        'queryset' : animals
    }
    return render(request, 'animals.html', context)


def register(request):
    return render(request, 'register.html')
# Create your views here.
