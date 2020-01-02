from django.shortcuts import render
from .models import Animal


def index(request):
    animals = Animal.objects.all()
    return render(request, 'index.html', {'animals': animals})

def register(request):
    return render(request, 'register.html')
# Create your views here.
