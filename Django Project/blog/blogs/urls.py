"""defines url patterns for blogs"""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('newblog/', views.newblog, name='newblog'),
    path('editblog/<int:entry_id>/', views.editblog, name='editblog'),
]
