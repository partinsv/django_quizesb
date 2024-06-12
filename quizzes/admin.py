from django.contrib import admin
from .models import Quiz, Question, Answer, UserAnswer, UserQuizResult, UserActivityLog

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'quiz', 'difficulty', 'question_type']
    list_filter = ['quiz', 'difficulty', 'question_type']
    inlines = [AnswerInline]

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(UserAnswer)
admin.site.register(UserQuizResult)
admin.site.register(UserActivityLog)
