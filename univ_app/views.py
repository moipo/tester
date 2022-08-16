from django.shortcuts import render, redirect
from .forms import *
from .models import *



# Create your views here.


class General:
    def base(request):
        return render(request, "very_first_page.html", {})

    def createtest_form(request):
        if request.method == "POST":
            form_result = TestForm(request.POST)
            if form_result.is_valid():
                Test.objects.create(**form_result.cleaned_data)
                return redirect('create_question')


        form_test = TestForm()
        ctx = {
            "form_test": form_test,
        }
        return render(request, "createtest_form.html", ctx)

    def createquestion_form(request):
        question_form = QuestionForm()
        ctx = {
            'question_form' : question_form,
        }
        return render(request, "createquestions_form.html", ctx)