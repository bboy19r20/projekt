from django import forms
from .models import Animal
from .models import Food
from .models import Type
from .models import Environment
from .models import Climate


class AddAnimal(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    eat = forms.ModelChoiceField(queryset=Food.objects, required=True)
    type = forms.ModelChoiceField(queryset=Type.objects, required=True)
    environment = forms.ModelChoiceField(queryset=Environment.objects, required=True)
    climate = forms.ModelChoiceField(queryset=Climate.objects, required=True)
    image_url = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))


