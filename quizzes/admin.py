from django.contrib import admin
from .models import Quiz, Question

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Количество пустых вопросов для добавления

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
