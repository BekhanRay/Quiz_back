
from django.contrib import admin
from django.contrib.auth import models
from .models import Category, Choice, Quiz, Question


admin.site.unregister(models.Group)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Question)
class Question(admin.ModelAdmin):
    list_display = ('quiz', 'question_text',)
    search_fields = ('quiz',)
    inlines = [ChoiceInline]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'description', 'image', 'date_published')
    list_filter = ('category', 'date_published')
    search_fields = ('category', 'title', 'description')
    date_hierarchy = 'date_published'
    ordering = ('category', 'date_published')

    class Meta:
        model = Quiz
        fields = ('category', 'title', 'description', 'image', 'date_published')
        readonly_fields = ('date_published',)
        fieldsets = (
            (None, {'fields': ('category', 'title', 'description', 'date_published')}),
            ('Image', {'fields': ('image',)})

        )


