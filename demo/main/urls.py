from django.urls import path, include
from . import views

#appname = main

urlpatterns = [
    path('', views.mainview, name = 'main'),
    path('add/', views.addview, name = 'add')
]
