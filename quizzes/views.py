from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, UserAnswer

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quizzes/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()
    return render(request, 'quizzes/quiz_detail.html', {'quiz': quiz, 'questions': questions})

def question_detail(request, quiz_id, question_id):
    question = get_object_or_404(Question, id=question_id, quiz_id=quiz_id)
    
    if request.method == 'POST':
        selected_option = request.POST.get('answer')
        correct = selected_option == question.correct_option
        UserAnswer.objects.create(
            question=question,
            selected_option=selected_option,
            correct=correct
        )

        next_question = Question.objects.filter(quiz_id=quiz_id, id__gt=question_id).first()
        
        if next_question:
            return redirect('question_detail', quiz_id=quiz_id, question_id=next_question.id)
        else:
            return redirect('quiz_results', quiz_id=quiz_id)
    
    return render(request, 'quizzes/question_detail.html', {'question': question})

def quiz_results(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    user_answers = UserAnswer.objects.filter(question__quiz=quiz)
    total_questions = user_answers.count()
    correct_answers = user_answers.filter(correct=True).count()
    incorrect_answers = user_answers.filter(correct=False)
    return render(request, 'quizzes/quiz_results.html', {
        'quiz': quiz,
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'incorrect_answers': incorrect_answers,
    })
