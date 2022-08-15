from django.shortcuts import render
from .forms import TestForm
# Create your views here.


class General:
    def base(request):
        return render(request, "base.html", {} )

    def createtest(request):
        form_test = TestForm()
        ctx = {
            "form_test": form_test,
        }
        return render(request, "createtest.html", ctx )