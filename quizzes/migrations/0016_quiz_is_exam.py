# Generated by Django 5.0.6 on 2024-06-14 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0015_alter_quizaccess_unique_together_quizaccess_quizzes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='is_exam',
            field=models.BooleanField(default=False),
        ),
    ]
