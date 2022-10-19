from django.contrib import admin
from django.urls import path
from pagat import views

urlpatterns = [
    path('', views.prova, name='home'),
    path('neto', views.paganeto, name='neto'),
]