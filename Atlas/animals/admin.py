from django.contrib import admin
from .models import Animal
from .models import Food
from .models import Continent
from .models import Type
from .models import Environment
from .models import Climate


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'eat')

class FoodAdmin(admin.ModelAdmin):
    list_display = ['type']

class ContinentAdmin(admin.ModelAdmin):
    list_display = ['type']

class TypeAdmin(admin.ModelAdmin):
    list_display = ['type']

class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ['type']

class ClimateAdmin(admin.ModelAdmin):
    list_display = ['type']




admin.site.register(Food, FoodAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Continent, ContinentAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Environment, EnvironmentAdmin)
admin.site.register(Climate, ClimateAdmin)
# Register your models here.
