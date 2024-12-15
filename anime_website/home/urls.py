from django.shortcuts import redirect
from django.views.generic.base import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
]