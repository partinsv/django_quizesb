from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('quiz/<int:quiz_id>/results/', views.quiz_results, name='quiz_results'),
]
