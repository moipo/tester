from django.urls import path
from .views import *

urlpatterns = [
    path('',General.base),
    path('createtest/',General.createtest_form),
    path('create_questions/',General.createquestion_form, name = "create_question"),
]