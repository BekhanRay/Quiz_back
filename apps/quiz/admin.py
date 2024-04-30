
from django.contrib import admin
from .forms import ResultsForm
from .models import Choice, Quiz, Question, Result


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = ('quiz', 'question_text',)
    search_fields = ('quiz',)
    inlines = [ChoiceInline]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date_published')
    list_filter = ('date_published',)
    search_fields = ('title', 'description')
    date_hierarchy = 'date_published'
    ordering = ('date_published',)

    class Meta:
        model = Quiz
        fields = ('title', 'description', 'date_published')
        readonly_fields = ('date_published',)


# admin.site.register(Result)
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    form = ResultsForm
    list_display = ('user', 'quiz', 'score', 'total_questions', 'date',)
    list_filter = ('user', 'quiz', 'score',)