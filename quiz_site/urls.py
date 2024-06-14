from django.contrib import admin
from django.urls import path, include
from quizzes import views as quiz_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', quiz_views.index, name='index'),  # Главная страница с анимацией
    path('quizzes/', include('quizzes.urls')),  # Страница со списком тестов
]
