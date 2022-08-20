from django.urls import path
from .views import *

urlpatterns = [
    path('',General.base),
    path('newtest/',General.createtest_form, name = 'newtest'),
    path('newtest/<int:testid>/create_questions/',General.createquestions_form, name = "newquestions"),
    path('geturl/<int:testid>', General.geturl, name = "geturl"),
    path('take_a_test/<int:testid>', General.take_a_test, name = "take_a_test")
    # path('add_answer/', General.add_answer, name = 'add_answer'),
]
# <int:testid>
# как конструируется паттерн
# как сделать аргумент опциональным
