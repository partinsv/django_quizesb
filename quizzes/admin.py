from django.contrib import admin
from .models import Quiz, Question

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Количество пустых вопросов для добавления
    fields = ['text', 'option1', 'option2', 'option3', 'option4', 'correct_option', 'difficulty']

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'quiz', 'difficulty']
    list_filter = ['quiz', 'difficulty']

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
