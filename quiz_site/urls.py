from django.contrib import admin
from django.urls import include, path
from quizzes import views as quiz_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quizzes.urls')),
    path('accounts/', include('accounts.urls')),  # Добавлено
    path('register/', quiz_views.register, name='register'),
    path('profile/', quiz_views.profile, name='profile'),
    path('activity_log/', quiz_views.activity_log, name='activity_log'),
]
