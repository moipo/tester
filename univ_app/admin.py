from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Answer)
admin.site.register(Question)
# admin.site.register(Test)
# admin.site.register(User)


class TestAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "slug"]

admin.site.register(Test, TestAdmin)

class TakenTestAdmin(admin.ModelAdmin):
    list_display = ["id", "related_test", "score"]

class AnsweredQuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "related_taken_test", "related_question", "correct"]

class GivenAnswerAdmin(admin.ModelAdmin):
    list_display = ["id","related_answered_question" , "checked"]

admin.site.register(TakenTest,TakenTestAdmin)
admin.site.register(AnsweredQuestion,AnsweredQuestionAdmin)
admin.site.register(GivenAnswer,GivenAnswerAdmin)
