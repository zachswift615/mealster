from django.contrib import admin
from .models import UnitOfMeasure, MealItem, Meal, Ingredient
# Register your models here.
admin.site.register(UnitOfMeasure)
admin.site.register(MealItem)
admin.site.register(Meal)
admin.site.register(Ingredient)

