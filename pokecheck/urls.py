from django.urls import path, include
from . import views

urlpatterns = [
    path('check/', views.pokecheck, name='pokecheck'),

]
