# Generated by Django 5.0.6 on 2024-06-12 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0012_alter_userprofile_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.organization')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiz')),
            ],
            options={
                'unique_together': {('quiz', 'organization')},
            },
        ),
    ]
