from django.contrib import admin
from .models import Animal
from .models import Food


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'eat')


class FoodAdmin(admin.ModelAdmin):
    list_display = ['type']

admin.site.register(Food, FoodAdmin)
admin.site.register(Animal, AnimalAdmin)
# Register your models here.
