from .models import *
from django import forms

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = [
            'title',
            'description',
        ]

        labels = {
            "title" : "Название теста",
            "description" : "Описание",
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'question',
            'importance',
        ]

        labels = {
            "question" : "Текст вопроса",
            "importance" : "Очков за вопрос (важность вопроса)",
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'answer',
            'is_right',
        ]