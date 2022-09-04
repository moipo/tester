from django.urls import path
from .views import *

urlpatterns = [
    path('',General.base),
    path('newtest/',General.createtest_form, name = 'newtest'),
    path('newtest/<int:testid>/create_questions/',General.createquestions_form, name = "newquestions"),
    path('geturl/<int:testid>', General.geturl, name = "geturl"),
    path('take_a_test/<int:testid>', General.take_a_test, name = "take_a_test"),
    path('take_a_test/<int:testid>/test_taking/<int:current_question>', General.test_taking, name = "test_taking"),
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
