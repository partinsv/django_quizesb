from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Organization, Department, UserProfile

class UserRegisterForm(UserCreationForm):
    organization = forms.ModelChoiceField(queryset=Organization.objects.all())
    department = forms.ModelChoiceField(queryset=Department.objects.all())

    class Meta:
        model = User
        fields = ['username', 'organization', 'department', 'password1', 'password2']
