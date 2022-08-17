from django.urls import path
from .views import *

urlpatterns = [
    path('',General.base),
    path('createtest/',General.createtest_form, name = 'createtest'),
    path('createtest/<int:testid>/create_questions/',General.createquestion_form, name = "createtest"),
    path('add_answer/', General.add_answer, name = 'add_answer'),
]

# как конструируется паттерн
# как сделать аргумент опциональным