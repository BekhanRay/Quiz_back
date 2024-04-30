from django import forms

from .models import Result


class ResultsForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['user', 'quiz', 'score', 'total_questions', 'right_answers',]

