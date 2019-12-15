from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log),
    path('sign/', views.sign),
    path('', views.index),
    path('logout/', views.out),
    path('add/', views.add)
]