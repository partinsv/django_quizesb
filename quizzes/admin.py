from django.contrib import admin
from .models import Quiz, Question, UserAnswer, UserQuizResult, UserActivityLog

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Количество пустых вопросов для добавления

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'quiz', 'difficulty']
    list_filter = ['quiz', 'difficulty']

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserAnswer)
admin.site.register(UserQuizResult)
admin.site.register(UserActivityLog)
