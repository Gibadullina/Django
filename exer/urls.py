from django.urls import path
from exer import views

urlpatterns = [
    path('time/', views.index),
]
