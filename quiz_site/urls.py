from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from quizzes import views as quiz_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quizzes.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', quiz_views.register, name='register'),
    path('profile/', quiz_views.profile, name='profile'),
]
