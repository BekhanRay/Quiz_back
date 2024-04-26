from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Quiz(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def upload_to(self, filename):
        filename = '_'.join(filename.split())
        return f'quiz/{self.category}/{self.title}/{filename}'

    image = models.ImageField(upload_to=upload_to, blank=True)

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


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
