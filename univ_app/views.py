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
                # Test.objects.create(**form_result.cleaned_data)
                # return redirect('create_question')
                model_instance = form_result.save()
                # return redirect(result)
                # return render(request, 'createquestions_form', {})
                print(model_instance.pk)
                # print(Test.objects.filter(request))
                return redirect('newquestions',model_instance.pk)


        form_test = TestForm()
        ctx = {
            "form_test": form_test,
        }
        return render(request, "createtest_form.html", ctx)

    def createquestions_form(request, testid):
        if request.method == "POST":
            question_form = QuestionForm(request.POST)
            answer1_form = AnswerForm(request.POST)
            answer2_form = AnswerForm(request.POST)
            print("it's ok 2")
            if all([question_form.is_valid(), answer1_form.is_valid(), answer2_form.is_valid()]):
                # print(question_form)
                question = question_form.save()
                # print(Test.objects.all().get(id = testid))
                question.related_test = Test.objects.all().get(id = testid)
                question.save()
                # print(question)
                answer1 = answer1_form.save()
                answer1.related_question = question
                answer1.save()
                answer2 = answer2_form.save()
                answer2.related_question = question
                answer2.save()
                # print("is valid")
        answer_form = AnswerForm()
        question_form = QuestionForm()
        ctx = {
            'question_form' : question_form,
            'answer_form' : answer_form,
        }
        return render(request, "createquestions_form.html", ctx)

    def geturl(request):
        return render(request,"geturl.html",{})

    # def add_answer(request):
    #
    #     Answer.objects.create()
    #     ctx = {
    #         'question_form' : question_form,
    #     }
    #     return render(request, "createquestions_form.html", ctx)
