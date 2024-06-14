from django.contrib import admin
from .models import Organization, Department, UserProfile, Quiz, Question, Answer, UserAnswer, UserQuizResult, UserActivityLog, QuizAccess, UserExamAccess

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization')
    list_filter = ('organization',)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'organization', 'department')
    list_filter = ('organization', 'department')
    search_fields = ('user__username',)

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
    list_display = ['title', 'is_exam', 'duration']
    list_filter = ['is_exam', 'duration']

class QuizAccessAdmin(admin.ModelAdmin):
    list_display = ('organization', 'department')
    list_filter = ('organization', 'department')
    filter_horizontal = ('quizzes',)  # For ManyToManyField

class UserExamAccessAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'granted_at')
    list_filter = ('quiz', 'user')
    search_fields = ('user__username', 'quiz__title')

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(UserAnswer)
admin.site.register(UserQuizResult)
admin.site.register(UserActivityLog)
admin.site.register(QuizAccess, QuizAccessAdmin)
admin.site.register(UserExamAccess, UserExamAccessAdmin)
