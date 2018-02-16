from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Meal, MealItem, Ingredient, UnitOfMeasure


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meal
        fields = ('name', 'serves', ) #'meal_items',


class MealItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MealItem
        fields = ('name', 'quantity')
