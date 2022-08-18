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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #parent class
        self.fields['answer'].widget.attrs.update(
        {'class': 'form-control',
         'style':'width:400px; height:25px;  display:inline-block;',
         })
        self.fields['is_right'].widget.attrs.update({'class': 'form-check-input',
        "style": "display:inline-block;"})

    class Meta:
        model = Answer
        fields = [
            'answer',
            'is_right',
        ]
        widgets = {

        }
