"""Defines URLs for pizzas"""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('pizzas/', views.pizzas, name='pizzas'),
]