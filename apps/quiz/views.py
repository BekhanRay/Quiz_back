
from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Result
from .forms import ResultsForm


def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})


def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    Result.objects.filter(user=request.user, quiz=quiz).delete()
    return render(request, 'quiz_detail.html', {'quiz': quiz})


def quiz_attempt(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == 'POST':
        right_answers = 0
        total_questions = quiz.question_set.count()
        for question in quiz.question_set.all():
            selected_choice_id = request.POST.get(f'question{question.id}')
            if selected_choice_id:
                selected_choice = question.choice_set.get(pk=selected_choice_id)
                if selected_choice.is_correct:
                    right_answers += 1
        score = (right_answers / total_questions) * 100
        score = round(score, 2)
        results = Result.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            total_questions=total_questions,
            right_answers=right_answers,
        )

        results.save()
        return redirect('result', quiz_id=quiz.id)
    return render(request, 'quiz_attempt.html', {'quiz': quiz})


def result_view(request, quiz_id):
    result = Result.objects.filter(user=request.user, quiz=quiz_id).last()
    return render(request, 'result.html', {'result': result})
