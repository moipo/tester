from .models import *
from django import forms

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = [
            'title',
            'description',
        ]