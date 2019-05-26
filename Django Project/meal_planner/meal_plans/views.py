from django.shortcuts import render

def index(request):
    """This is the home page for the Meal Planner"""
    return render(request, 'meal_plans/index.html')