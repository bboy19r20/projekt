from django import forms
from .models import Animal
from .models import Food
from .models import Type
from .models import Environment
from .models import Climate

default_error_list = {
  'required': 'Wymagane',
  'invalid': 'Błędny adres',
}


class AddAnimal(forms.Form):
    Nazwa = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    Jedzenie = forms.ModelChoiceField(queryset=Food.objects, required=True)
    Typ = forms.ModelChoiceField(queryset=Type.objects, required=True)
    Środowisko = forms.ModelChoiceField(queryset=Environment.objects, required=True)
    Klimat = forms.ModelChoiceField(queryset=Climate.objects, required=True)
    Obraz_URL = forms.URLField(required=True, error_messages=default_error_list)


