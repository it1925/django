from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.student_show, name = 'student_show'),
]