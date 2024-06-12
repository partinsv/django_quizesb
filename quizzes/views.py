from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Answer, UserAnswer, UserQuizResult, UserActivityLog
import random

def log_user_activity(user, activity):
    UserActivityLog.objects.create(user=user, activity=activity)

def quiz_list(request):
    if request.user.is_authenticated:
        log_user_activity(request.user, "Viewed quiz list")
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
            selected_answers = request.POST.getlist(f'question_{question.id}')
            selected_answer_objs = Answer.objects.filter(id__in=selected_answers)
            correct = all(ans.is_correct for ans in selected_answer_objs) and len(selected_answer_objs) > 0
            user_answers[str(question.id)] = {
                'selected_answers': [ans.id for ans in selected_answer_objs],
                'correct': correct
            }
        request.session['user_answers'] = user_answers
        log_user_activity(request.user, f"Submitted answers for quiz {quiz.title}")
        return redirect('quiz_results', quiz_id=quiz_id)

    log_user_activity(request.user, f"Started quiz {quiz.title}")
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
            'selected_answers': Answer.objects.filter(id__in=incorrect_answers[str(question.id)]['selected_answers'])
        })

    UserQuizResult.objects.create(
        user=request.user,
        quiz=quiz,
        total_questions=total_questions,
        correct_answers=correct_answers,
        completed_at=timezone.now()
    )

    request.session.pop('user_answers', None)
    request.session.pop('questions', None)

    log_user_activity(request.user, f"Completed quiz {quiz.title}")
    return render(request, 'quizzes/quiz_results.html', {
        'quiz': quiz,
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'incorrect_answers_details': incorrect_answers_details,
    })

@login_required
def user_statistics(request):
    log_user_activity(request.user, "Viewed user statistics")
    user_results = UserQuizResult.objects.filter(user=request.user).order_by('-completed_at')
    return render(request, 'quizzes/user_statistics.html', {'user_results': user_results})

@login_required
def activity_log(request):
    if not request.user.is_staff:
        return redirect('quiz_list')
    logs = UserActivityLog.objects.all().order_by('-timestamp')
    return render(request, 'quizzes/activity_log.html', {'logs': logs})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            log_user_activity(request.user, "Registered a new account")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    log_user_activity(request.user, "Viewed profile")
    user_results = UserQuizResult.objects.filter(user=request.user).order_by('-completed_at')
    return render(request, 'registration/profile.html', {'user_results': user_results})
