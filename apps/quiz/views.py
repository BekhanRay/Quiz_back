
from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Category, Choice


def QuizList(request):
    quiz_list = Quiz.objects.all()

    return render(request, 'quiz.html', context={'quiz_list': quiz_list})


def QuizDetail(request, quiz_id):
    if quiz_id == 0:
        quiz = Quiz.objects.first()
    else:
        quiz = get_object_or_404(Quiz, pk=quiz_id)

    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        if choice_id:
            choice = get_object_or_404(Choice, pk=choice_id)
            # Save the user's choice
            choice.answer.add(request.user)
        # Redirect to the next question or quiz completion page
        # Here, you need to implement the logic for fetching the next question
        # For now, let's assume we just go to the next question
        return redirect('next_question', quiz_id=quiz.id)
    return render(request, 'quiz_details.html', {'quiz': quiz})


def next_question(request, quiz_id):
    return redirect('quiz_detail', quiz_id=quiz_id)