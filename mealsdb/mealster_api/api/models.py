from django.db import models

# Create your models here.


class UnitOfMeasure(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit_of_measure = models.ForeignKey(
        UnitOfMeasure, on_delete=models.CASCADE,
        blank=True, null=True
    )

    def __str__(self):
        return self.name


class MealItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.CharField(max_length=255)
    serves = models.IntegerField(blank=True, null=True)
    meal_items = models.ManyToManyField(MealItem)

    def __str__(self):
        return self.name


