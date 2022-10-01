from .models import *
from django import forms
from django.contrib.auth.models import User


class ChangeUserForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()

    def clean_first_name(self):
        cleaned_data = self.cleaned_data #dictioary
        first_name = cleaned_data.get('first_name')
        if first_name.strip() == "Ivan": #Владиация немодельных форм.
            raise forms.ValidationError("This name is taken")
        return cleaned_data


    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        return cleaned_data



class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = [
            'title',
            'description',
            'image',
        ]

        labels = {
            "title" : "Название теста",
            "description" : "Описание",
            'image': "Картинка",
        }

# class AnswerFormNotModel(forms.Form):
#     answer = forms.CharField(max_length=1000)
#     was_chosen = forms.BooleanField()
#     is_right = forms.BooleanField()
#     related_question = forms.ModelChoiceField #integerField





class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'question',
        ]

        labels = {
            "question" : "Текст вопроса",
        }



class AnswerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #parent class
        self.fields['answer'].widget.attrs.update(
        {'class': 'form-control',
         'style':' placeholder : "Вопрос"; width:700px; height:25px;  display:inline-block;',
         })
        self.fields['is_right'].widget.attrs.update({'class': 'form-check-input',
        "style": " display:inline-block;"})

    class Meta:
        model = Answer
        fields = [
            'answer',
            'is_right',
        ]

        labels = {
            "is_right" : "Ответ является правильным ",
            'answer': "Ответ",
        }



class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #parent class
        self.fields['username'].widget.attrs.update(
        {'class': 'form-control',
         'style':' placeholder : "Логин"',})
        self.fields['password'].widget.attrs.update(
        {'class': 'form-control',
         'style':' placeholder : "Пароль"',})

    class Meta:
        model = User
        fields = [
        'username',
        'password',
        ]
