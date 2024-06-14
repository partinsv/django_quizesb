from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/results/', views.quiz_results, name='quiz_results'),
    path('statistics/', views.user_statistics, name='user_statistics'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('activity_log/', views.activity_log, name='activity_log'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('exams/', views.exam_list, name='exam_list'),  # Добавлен новый маршрут
]
