from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('personal/<int:num>', views.personal),
    path('filtering', views.filtering)
]
