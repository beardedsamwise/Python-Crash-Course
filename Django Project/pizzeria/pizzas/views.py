from django.shortcuts import render

def index(request):
    """Home page for Pizzeria"""
    return render(request, 'pizzas/index.html')