# Generated by Django 5.0.6 on 2024-06-09 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_quiz_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='duration',
        ),
    ]
