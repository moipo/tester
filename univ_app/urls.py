from django.urls import path
from .views import *

urlpatterns = [
    path('',General.base),
    path('newtest/',General.createtest_form, name = 'newtest'),
    path('newtest/<int:testid>/create_questions/',General.createquestions_form, name = "newquestions"),
    path('geturl/<int:testid>', General.geturl, name = "geturl"),
    path('start_a_test/<int:testid>', General.start_a_test, name = "start_a_test"),
    path('start_a_test/<int:testid>/take_test/<int:current_question_num>', General.test_taking, name = "take_test"),
    path('login/', General.login_form, name = "login_form"),
    path('register/', General.register, name = "register"),
    path('log_out/', General.log_out, name = "log_out"),
    path('statistics/', General.statistics, name = "statistics"),
    path('login_required/', General.access_denied, name = "access_denied"),
    path('show_my_profile/', General.show_my_profile, name = "show_my_profile"),
    path('show_change_user_credentials/', General.show_change_user_credentials, name = "show_change_user_credentials"),

    # path('show_my_profile', General.show_my_profile, name = "show_my_profile"),
    # path('add_answer/', General.add_answer, name = 'add_answer'),
]
# <int:testid>
# как конструируется паттерн
# как сделать аргумент опциональным
