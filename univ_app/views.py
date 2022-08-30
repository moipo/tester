from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
#проблема такого(*) импорта в том, что все импортированные библиотеки тоже сюда импортируются
from .models import *
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse # для начальной разметки
from django.contrib.auth.decorators import login_required
#add: login_required, form




# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class General:
    def base(request):
        ctx = {
        "state_of_user" : request.user.is_authenticated
        }

        return render(request, "very_first_page.html", ctx)

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
        answer_form1 = AnswerForm() #костыль
        answer_form2 = AnswerForm()
        answer_form3 = AnswerForm()
        answer_form4 = AnswerForm()
        # answer_form_set = [answer_form1,answer_form2,answer_form3,answer_form4]
        question_form = QuestionForm()
        previous_questions = Question.objects.filter(related_test = Test.objects.get(id=testid))
        ctx = {
            'question_form' : question_form,
            'answer_form1':AnswerForm(),
            'answer_form2':answer_form2,
            'answer_form3':answer_form3,
            'answer_form4':answer_form4,
            'previous_questions': previous_questions,
            'testid': testid,
        }
        return render(request, "createquestions_form.html", ctx)

    def geturl(request, testid):

        print(request.get_host)
        path = reverse(General.start_a_test, args = [testid])
        yoururl = str(request.META["HTTP_HOST"])  + str(path)
        ctx = {
        "testid":testid,
        "yoururl": yoururl,
        }


        return render(request, "geturl.html", ctx)


    def start_a_test(request, testid):
        the_test = Test.objects.get(id = testid)
        the_questions = Question.get_test_questions(the_test)
        ctx = {
        "the_test":the_test,
        "the_questions" : the_questions,
        }
        return render(request,"test_taking/start_a_test.html", ctx )


    def test_taking(request, testid, current_question_num):
        the_test = Test.objects.get(pk = testid)
        question_set = Question.get_test_questions(the_test)
        this_question = None

        this_question = question_set[current_question_num] #current_question_num
        next_question_num = current_question_num + 1
        if len(question_set) < next_question_num:
            next_question = 999999 #finishthetest

        the_answers = Answer.get_answers(this_question)
        ctx = {
            "this_question": this_question,
            "next_question_num": next_question_num,
            "the_answers" : the_answers,
            "the_test" : the_test,
            "test_len" : len(question_set)
        }
        return render(request,"test_taking/test_taking.html", ctx )


    def login_form(request):
        if request.method == "POST": #елси это POST, значит мы берем инфу из секции POST
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username = username, password = password)
            if user is None:

                user_form = UserForm()
                ctx = {
                'error' : "Invalid username or password",
                "user_form" : user_form,
                }
                  #asdf adsf - пользователь
                return render(request, "sign/login_form.html", ctx)
            else:
                login(request,user)
                ctx = {
                    "user" : user,
                }
                return render(request, "profile/myprofile.html", ctx)

        else:
            user_form = UserForm()
            ctx = {
            "user_form" : user_form,
            }
            return render(request, "sign/login_form.html", ctx)



    def register(request):
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username = username, password = password)
            if user is None:
                user = User.objects.create_user(username = username, password = password)
                ctx = {
                    "user" : user,
                }
                return render(request, "profile/myprofile.html", ctx)
            else:
                user_form = UserForm()
                ctx = { "error" :
                "Такой пользователь уже существует! Используйте другой логин.",
                "user_form" : user_form,
                }
                return render(request, "sign/register.html", ctx)

        else:
            user_form = UserForm()
            ctx = {
            "user_form" : user_form,
            }
            return render(request, "sign/register.html", ctx)

    def log_out(request):
        if request.user.is_authenticated:
            logout(request)
        return redirect(General.base)

    @login_required(login_url = "/login_required/")
    def statistics(request):
        content = "<h1> СТАТИСТИКА ОТВЕТОВ НА ТЕСТЫ </h1>"
        return HttpResponse(content)

    def access_denied(request):
        return render(request,"login_required_redirect.html",{})




































            #regiester
            # user = User.objects.create_user(username = username, password = password)
            # print(user)
            # return HttpResponse("<h1> homepage <h1>")
            # return redirect(General.show_my_profile)



    # def show_my_profile(request, user):
        # ctx = {
        #     "user" : user,
        # }
        # return render(request, "profile/myprofile.html", ctx)


            # # user_form = UserForm(request.POST)
            # print(request.POST)
            # if user_form.is_valid():
            #     print(user_form.cleaned_data)
            #     user = User.objects.create_user(**user_form.cleaned_data)
            #     print(user)
            # else:
            #     print("User form is not valid")
            # user_form = UserForm()
            # ctx = {
            # "user_form" : user_form,
            # "HTTPRESPONSE" : request.POST,
            # }
            # return render(request, "sign/signinup.html", ctx)
        # else:
        #     user_form = UserForm()
        #     ctx = {
        #     "user_form" : user_form,
        #     # "HTTPRESPONSE" : request.META,
        #     }
        #     return render(request, "sign/signinup.html", ctx)


    # def add_answer(request):
    #
    #     Answer.objects.create()
    #     ctx = {
    #         'question_form' : question_form,
    #     }
    #     return render(request, "createquestions_form.html", ctx)
