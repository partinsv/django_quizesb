from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    QUESTION_TYPE_CHOICES = [
        ('single', 'Single Choice'),
        ('multiple', 'Multiple Choice'),
    ]

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=6, choices=DIFFICULTY_CHOICES, default='medium')
    question_type = models.CharField(max_length=8, choices=QUESTION_TYPE_CHOICES, default='single')

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text} - {self.text}"

class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answers = models.ManyToManyField(Answer)
    correct = models.BooleanField()

    def __str__(self):
        return f'{self.question.text} - {self.correct}'

class UserQuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    total_questions = models.IntegerField()
    correct_answers = models.IntegerField()
    completed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - {self.quiz.title} - {self.correct_answers}/{self.total_questions}'

class UserActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - {self.activity} - {self.timestamp}'
