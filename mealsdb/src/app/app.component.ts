import { Component } from '@angular/core';

class MealItem {
  name?: string;
}
class Meal {
  name?: string;
  mealItems?: MealItem[];
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})


export class AppComponent {
  title = 'app';
  meal: Meal = {};
  selected: any = {};
  meals = [];
  mealItem: MealItem = {};
  mealItems: MealItem[] = [
    {name: 'Tacos'},
    {name: 'Burgers'},
    {name: 'Sweet Potatoes'},
    {name: 'Okra'},
    {name: 'Salad'}
  ];
  addMeal() {
    this.meals.push(this.meal);
    this.meal = {}
  }

  addMealItem() {
    this.mealItems.push(this.mealItem);
    this.mealItem = {};
  }

  addItemToMeal() {
    debugger;
    if (!this.meal.mealItems || !this.meal.mealItems.length) {
      this.meal.mealItems = [];
    }
    this.meal.mealItems.push(this.selected.mealItem);
  }
}
