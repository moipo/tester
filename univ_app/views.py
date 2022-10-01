from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required







class General:

    def homepage(request):
        ctx = {
        "state_of_user" : request.user.is_authenticated
        }
        return render(request, "homepage/homepage.html", ctx)


    def create_test(request):
        if request.method == "POST":
            form_result = TestForm(request.POST)
            if form_result.is_valid():
                test_instance = form_result.save()
                return redirect('create_questions', test_instance.pk)


        form_test = TestForm()
        ctx = {
            "form_test": form_test,
        }
        return render(request, "create_test/create_test.html", ctx)

    def create_questions(request, testid):
        if request.method == "POST":
            print(request.POST)

            the_test = Test.objects.get(id = testid)
            previous_questions = Question.get_test_questions(the_test)

            answer_form_not_model = AnswerFormNotModel()
            ctx = {
            "answer_form_not_model" : answer_form_not_model,
            'testid': testid,
            'previous_questions' : previous_questions,
            }
            return render(request,"create_test/create_questions.html", ctx)

        else:
            answer_form_not_model = AnswerFormNotModel()
            ctx = {
            "answer_form_not_model" : answer_form_not_model,
            'testid': testid,
            }
            return render(request,"create_test/create_questions.html", ctx)

    # def create_questions(request, testid):
    #     if request.method == "POST":
    #         pass
    #
    #     answer_form = AnswerForm()
    #     ctx = {
    #     "answer_form" : answer_form,
    #     'testid': testid,
    #     }
    #     return render(request,"create_test/create_questions.html", ctx)


    def geturl(request, testid):
        path = reverse(General.start_a_test, args = [testid])
        yoururl = str(request.META["HTTP_HOST"])  + str(path)
        ctx = {
        "testid":testid,
        "yoururl": yoururl,
        }
        return render(request, "create_test/geturl.html", ctx)



    def start_a_test(request, testid):
        the_test = Test.objects.get(id = testid)
        the_questions = Question.get_test_questions(the_test)
        ctx = {
        "the_test":the_test,
        "the_questions" : the_questions,
        }
        return render(request,"take_test/start_a_test.html", ctx )


    def test_taking(request, testid, current_question_num):
        the_test = Test.objects.get(pk = testid)
        question_set = Question.get_test_questions(the_test)
        this_question = None

        this_question = question_set[current_question_num]
        next_question_num = current_question_num + 1
        if len(question_set) < next_question_num:
            next_question = 999999

        the_answers = Answer.get_answers(this_question)
        ctx = {
            "this_question": this_question,
            "next_question_num": next_question_num,
            "the_answers" : the_answers,
            "the_test" : the_test,
        }
        return render(request,"take_test/take_test.html", ctx )


    def login_form(request):
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username = username, password = password)
            if user is None:
                user_form = UserForm()
                ctx = {
                'error' : "Invalid username or password",
                "user_form" : user_form,
                }
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
        return render(request,"sign/login_required_redirect.html",{})



    def show_change_user_credentials(request):
        form = ChangeUserForm()
        ctx = {
            "form":form
        }
        if request.method == "POST":
            form = ChangeUserForm(request.POST)
            ctx['form'] = form
            if form.is_valid():
                print("form is valid")
                first_name = form.cleaned_data.get("first_name")
                last_name = form.cleaned_data.get("last_name")
                this_user = request.user
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                return redirect(General.show_my_profile)
        return render(request, "profile/change_user_credentials.html", ctx)



    def show_my_profile(request):
        ctx = {
            "user" : request.user,
        }
        return render(request, "profile/show_my_profile.html", ctx)
