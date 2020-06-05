from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from api import views 

urlpatterns = [
    path('students/', views.student_list),
    path('students/<int:pk>/', views.student_detail),
    path('dict/', views.dict_list),
    path('dict/<int:pk>/', views.dict_detail),
]
