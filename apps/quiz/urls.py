# urls.py

from django.urls import path
from .views import QuizList, QuizDetail

urlpatterns = [
    path('quiz/', QuizList, name='quiz_list'),
    path('quiz/<int:quiz_id>/', QuizDetail, name='quiz_detail'),
]
