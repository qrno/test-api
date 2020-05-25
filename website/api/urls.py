from django.urls import path
from api import views

urlpatterns = [
    path('students/', views.student_list)
]
