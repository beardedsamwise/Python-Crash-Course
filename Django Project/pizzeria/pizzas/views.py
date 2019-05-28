from django.shortcuts import render

from .models import Pizza,Topping

def index(request):
    """Home page for Pizzeria"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Page to list all pizzas"""
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Page to list individual pizzas"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)

