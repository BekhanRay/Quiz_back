
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Quiz, Result

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quiz_detail.html', {'quiz': quiz})

def quiz_attempt(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == 'POST':
        score = 0
        total_questions = quiz.question_set.count()
        for question in quiz.question_set.all():
            selected_choice_id = request.POST.get(f'question{question.id}')
            if selected_choice_id:
                selected_choice = question.choice_set.get(pk=selected_choice_id)
                if selected_choice.is_correct:
                    score += 1
        percentage_score = (score / total_questions) * 100
        percentage_score = round(percentage_score, 2)
        Result.objects.create(
            user=request.user,
            quiz=quiz,
            score=percentage_score,
            total_questions=total_questions
        )
        messages.success(request, f'Quiz submitted successfully! Your score: {percentage_score}%')
        return redirect('quiz_list')
    return render(request, 'quiz_attempt.html', {'quiz': quiz})


def result_list(request):
    results = Result.objects.filter(user=request.user)
    return render(request, 'result_list.html', {'results': results})


def result_detail(request, quiz_id):
    result = Result.objects.filter(user=request.user, quiz_id=quiz_id).last()
    return render(request, 'result.html', {'result': result})