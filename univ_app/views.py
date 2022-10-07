from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.views.generic import ListView




class TestList(ListView):
    paginate_by = 10
    model = Test
    template_name = "storage/test_list.html"


class General:

    def homepage(request):
        ctx = {
        "state_of_user" : request.user.is_authenticated
        }
        return render(request, "homepage/homepage.html", ctx)


    def create_test(request):
        if request.method == "POST":
            form_result = TestForm(request.POST ) #, request.FILES
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

            question = request.POST.get('question')

            the_test = Test.objects.get(id = testid)
            previous_questions = Question.get_test_questions(the_test)


            the_question = Question.objects.create(question = question, related_test = the_test)

            answers = request.POST.getlist('answer')
            is_right = request.POST.getlist('is_right')
            print(answers)
            print(is_right)


            for number, answer in enumerate(answers, 1):
                 ans_obj = Answer()
                 ans_obj.answer = answer
                 ans_obj.is_right = str(number) in is_right
                 # print( number, " not in ", is_right, end = "    ")
                 # print(str(number) in is_right)
                 ans_obj.related_question = the_question
                 ans_obj.save()


            # answers = Answer.objects.filter(related_question = the_question)






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

        the_test = Test.objects.get(id = testid)
        the_test.link = yoururl
        the_test.save()

        ctx = {
        "testid":testid,
        "yoururl": yoururl,
        }

        return render(request, "create_test/geturl.html", ctx)



    def start_a_test(request, testid):
        the_test = Test.objects.get(id = testid)
        ctx = {
        "the_test":the_test,
        }
        return render(request,"take_test/start_a_test.html", ctx )


    def take_test(request, testid, current_question_num, taken_test_id):



        if request.method == 'POST':

            # получение вопросов
            the_test = Test.objects.get(pk = testid)
            question_set = Question.get_test_questions(the_test)
            this_question = None

            # отправка вопроса и номера следующего


            next_question_num = current_question_num + 1
            if len(question_set) < next_question_num-1:
                next_question = 999999
                print("ПРИСВОЕНИЕ СРАБОТАЛО")

            taken_test = TakenTest.objects.get(id = taken_test_id)


            GivenAnswerFormSet = inlineformset_factory(
            AnsweredQuestion,
            GivenAnswer,
            fields = ("checked",) ,
            labels = {"checked" : ""},
            can_delete_extra = False,
            extra = len(question_set),
            )

            formset = GivenAnswerFormSet(request.POST)
            print(request.POST)
            print()
            print(formset)
            print()
            print(formset.errors)
            print(formset.is_valid())
            print(formset.save())



            previous_question = question_set[current_question_num-1]

            prev_ans_quest = AnsweredQuestion()
            prev_ans_quest.related_taken_test = taken_test
            prev_ans_quest.related_question = previous_question
            prev_ans_quest.save()


            previous_answers = Answer.get_answers(previous_question)

            for i in range(len(previous_answers)):
                checked = request.POST.get(f"givenanswer_set-{i}-checked","off")
                given_answer = GivenAnswer()
                print(True if checked == "on" else False)
                given_answer.checked = True if checked == "on" else False
                print(given_answer.checked)
                given_answer.related_answered_question = prev_ans_quest
                given_answer.save()





            #was question answered right?
            all_prev_given_ans = GivenAnswer.objects.filter(related_answered_question = prev_ans_quest)

            prev_ans_quest.correct = all([ans.is_right == prev_ans.checked for ans, prev_ans in zip(previous_answers , all_prev_given_ans)])
            prev_ans_quest.save()

            # zip_comp = zip(previous_answers , all_prev_given_ans)
            # for ans, given_ans in zip_comp:
            #     print(ans.is_right, ' vs ', given_ans.checked)
            # print("-------------")

            # prev_ans_quest.correct = all([ans.checked for ans in all_prev_given_ans])

            # print(previous_given_answers)




            # print(formset.is_valid())
            # if formset.is_valid():
            # formset.save()

            #manual save:





            if current_question_num == 999999:
                return redirect(reverse('show_result', args=[taken_test_id]))
            try:
                this_question = question_set[current_question_num]
            except:
                return redirect(reverse('show_result', args=[taken_test_id]))




            the_answers = Answer.get_answers(this_question)
            answered_question = AnsweredQuestion(related_taken_test = taken_test, related_question = this_question)
            givenanswer_formset = GivenAnswerFormSet()
            a_ga_zipped = zip(the_answers, givenanswer_formset)





            ctx = {
                "quantity_of_questions" : len(question_set),
                "this_question": this_question,
                "next_question_num": next_question_num,
                "the_answers" : the_answers,
                "givenanswer_formset" : givenanswer_formset,
                "the_test" : the_test,
                "a_ga_zipped" : a_ga_zipped,
                "taken_test" : taken_test,
            }
            return render(request,"take_test/take_test.html", ctx )


        else:

            # 0 передается с представления start_a_test




            #если get метод, то мы прежде чем отренедреить представление
            #создадим тест



            # получение вопросов
            the_test = Test.objects.get(pk = testid)
            question_set = Question.get_test_questions(the_test)
            this_question = None

            # отправка вопроса и номера следующего
            this_question = question_set[current_question_num]
            next_question_num = current_question_num + 1
            if len(question_set) < next_question_num:
                next_question = 999999

            the_answers = Answer.get_answers(this_question)


            # taken_test = None
            # if taken_test_id == 0:
            #     taken_test = TakenTest.objects.create(related_test = the_test, score = 0)
            # if taken_test:
            #     pass
            # else:

            #taken_test_id не используется в get запросе
            taken_test = TakenTest.objects.create(score = 0, related_test = the_test)


            given_answer_form = GivenAnswerForm()



            answered_question = AnsweredQuestion(related_taken_test = taken_test, related_question = this_question)

            #formset

            #передаем конкретного родителя
            GivenAnswerFormSet = inlineformset_factory(
            AnsweredQuestion ,
            GivenAnswer,
            fields = ("checked",) ,
            labels = {"checked" : ""},
            can_delete_extra = False,
            extra =  len(the_answers))


            # data = {
            # 'form-TOTAL_FORMS': str(len(the_answers)),
            # 'form-INITIAL_FORMS': '0',
            # }

            givenanswer_formset = GivenAnswerFormSet()

            a_ga_zipped = zip(the_answers, givenanswer_formset)

            ctx = {
                "quantity_of_questions" : len(question_set),
                "this_question": this_question,
                "next_question_num": next_question_num,
                "the_answers" : the_answers,
                "givenanswer_formset" : givenanswer_formset,
                "the_test" : the_test,
                "a_ga_zipped" : a_ga_zipped,
                "taken_test" : taken_test,
            }
            return render(request,"take_test/take_test.html", ctx )


    def show_result(request, taken_test_id):
        taken_test = TakenTest.objects.get(pk = taken_test_id)
        answered_questions = AnsweredQuestion.objects.filter(related_taken_test = taken_test)
        taken_test.score = sum([1 if ans_question.correct else 0 for ans_question in answered_questions])
        taken_test.save()
        q_amount = len(answered_questions)
        ctx = {
        "taken_test":taken_test,
        "q_amount" : q_amount,
        }
        return render(request, "take_test/show_result.html", ctx)
    # def take_test(request, testid, current_question_num):
    #     if request.method == 'POST':
    #         print(request.POST)
    #         the_test = Test.objects.get(pk = testid)
    #         question_set = Question.get_test_questions(the_test)
    #         this_question = None
    #
    #         this_question = question_set[current_question_num]
    #         next_question_num = current_question_num + 1
    #         if len(question_set) < next_question_num:
    #             next_question = 999999
    #
    #         the_answers = Answer.get_answers(this_question)
    #         ctx = {
    #             "quantity_of_questions" : len(question_set),
    #             "this_question": this_question,
    #             "next_question_num": next_question_num,
    #             "the_answers" : the_answers,
    #             "the_test" : the_test,
    #         }
    #         return render(request,"take_test/take_test.html", ctx )
    #     else:
    #         the_test = Test.objects.get(pk = testid)
    #         question_set = Question.get_test_questions(the_test)
    #         this_question = None
    #
    #         this_question = question_set[current_question_num]
    #         next_question_num = current_question_num + 1
    #         if len(question_set) < next_question_num:
    #             next_question = 999999
    #
    #         the_answers = Answer.get_answers(this_question)
    #         ctx = {
    #             "quantity_of_questions" : len(question_set),
    #             "this_question": this_question,
    #             "next_question_num": next_question_num,
    #             "the_answers" : the_answers,
    #             "the_test" : the_test,
    #         }
    #         return render(request,"take_test/take_test.html", ctx )

    # def test_taking(request, testid, current_question_num):
    #     the_test = Test.objects.get(pk = testid)
    #     question_set = Question.get_test_questions(the_test)
    #     this_question = None
    #
    #     this_question = question_set[current_question_num]
    #     next_question_num = current_question_num + 1
    #     if len(question_set) < next_question_num:
    #         next_question = 999999
    #
    #     the_answers = Answer.get_answers(this_question)
    #     ctx = {
    #         "this_question": this_question,
    #         "next_question_num": next_question_num,
    #         "the_answers" : the_answers,
    #         "the_test" : the_test,
    #     }
    #     return render(request,"take_test/take_test.html", ctx )


    def show_result_table(request, taken_test_id):
        taken_test = TakenTest.objects.get(id = taken_test_id)
        answered_questions = AnsweredQuestion.objects.filter(related_taken_test =  taken_test)
        given_ans_arr2d = []
        for a_q in answered_questions:
            answers  = GivenAnswer.objects.filter(related_answered_question = a_q)
            given_ans_arr2d += [answers]


            #TakenTest.objects.filter(pk = taken_test.related_test)
        the_test = taken_test.related_test
        questions = Question.objects.filter(related_test = the_test)
        ans_arr2d = []
        #right_ans_arr2d = []
        for q in questions:
            answers = Answer.objects.filter(related_question = q)
            ans_arr2d += [answers]
            #right_ans_arr2d += [[answer for answer in answers if answer.is_right]]


        all_zipped = zip(questions,ans_arr2d,given_ans_arr2d,answered_questions)

        ctx = {
        "taken_test" : taken_test,
        "answered_questions" : answered_questions,
        "given_ans_arr2d" : given_ans_arr2d,
        "the_test": the_test,
        "questions":questions,
        "ans_arr2d":ans_arr2d,
        "all_zipped" : all_zipped,
        }
        return render(request, 'take_test/show_result_table.html', ctx)


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
