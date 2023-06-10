from django.urls import path
from . import views

urlpatterns = [

    path('questions', views.questions, name='questions'),
    path('', views.question, name='question'),
    path('check_answer/', views.check_answer, name='check_answer')
 
 ]
