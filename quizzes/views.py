from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Quiz, Question, UserAnswer, UserQuizResult
import random

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/quiz_list.html', {'quizzes': quizzes})

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if 'questions' not in request.session:
        all_questions = list(quiz.question_set.all())
        random.shuffle(all_questions)
        questions = all_questions[:2]
        request.session['questions'] = [q.id for q in questions]
    else:
        questions = Question.objects.filter(id__in=request.session['questions'])

    if request.method == 'POST':
        user_answers = request.session.get('user_answers', {})
        for question in questions:
            selected_option = request.POST.get(f'question_{question.id}')
            user_answers[str(question.id)] = {
                'selected_option': selected_option,
                'correct': selected_option == question.correct_option
            }
        request.session['user_answers'] = user_answers
        return redirect('quiz_results', quiz_id=quiz_id)

    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz, 'questions': questions})

@login_required
def quiz_results(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    user_answers = request.session.get('user_answers', {})
    total_questions = len(user_answers)
    correct_answers = sum(1 for answer in user_answers.values() if answer['correct'])
    incorrect_answers = {q_id: ans for q_id, ans in user_answers.items() if not ans['correct']}
    incorrect_questions = Question.objects.filter(id__in=incorrect_answers.keys())

    incorrect_answers_details = []
    for question in incorrect_questions:
        incorrect_answers_details.append({
            'question': question,
            'selected_option': incorrect_answers[str(question.id)]['selected_option']
        })

    UserQuizResult.objects.create(
        user=request.user,
        quiz=quiz,
        total_questions=total_questions,
        correct_answers=correct_answers
    )

    request.session.pop('user_answers', None)
    request.session.pop('questions', None)

    return render(request, 'quizzes/quiz_results.html', {
        'quiz': quiz,
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'incorrect_answers_details': incorrect_answers_details,
    })

@login_required
def user_statistics(request):
    user_results = UserQuizResult.objects.filter(user=request.user)
    return render(request, 'quizzes/user_statistics.html', {'user_results': user_results})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    user_results = UserQuizResult.objects.filter(user=request.user)
    return render(request, 'registration/profile.html', {'user_results': user_results})
