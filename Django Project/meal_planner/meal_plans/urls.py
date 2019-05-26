"""Defines URL patterns for learning logs."""

from django.urls import path

from . import views

app_name = 'meal_plans'
urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
]