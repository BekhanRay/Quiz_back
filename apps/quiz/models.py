from django.db import models
from apps.users.models import User

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def upload_to(self, filename):
        return f'{self.title}/{filename}'

    image = models.ImageField(upload_to=upload_to, blank=True, null=True)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.title

    def get_total_questions(self):
        return self.question_set.count()

    def get_total_answered_questions(self):
        return self.question_set.filter(choice__answer__isnull=False).distinct().count()

    def get_percentage_completed(self):
        total_questions = self.get_total_questions()
        if total_questions > 0:
            total_answered = self.get_total_answered_questions()
            return (total_answered / total_questions) * 100
        return 0


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

    def get_next_question(self):
        next_question = Question.objects.filter(quiz=self.quiz, id__gt=self.id).order_by('id').first()
        return next_question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    answered = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField(max_length=100)
    total_questions = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
