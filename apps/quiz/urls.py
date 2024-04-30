# urls.py

from django.urls import path
from apps.quiz import views


urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('<int:quiz_id>/attempt/', views.quiz_attempt, name='quiz_attempt'),
    path('<int:quiz_id>/result/', views.result_view, name='result')
]

