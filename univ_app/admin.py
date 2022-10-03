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

admin.site.register(TakenTest)
admin.site.register(AnsweredQuestion)
admin.site.register(GivenAnswer)
