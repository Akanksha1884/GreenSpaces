from django.contrib import admin
from django.urls import path
from . import views  # Import views module from the current directory

urlpatterns = [
    path('', views.dashboard, name='dashboard'), 
      # Define URL pattern for the dashboard view
    path('index', views.index, name='index'),
]
