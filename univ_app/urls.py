from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',General.homepage),
    path('create_test/',General.create_test, name = 'create_test'),
    path('create_test/<int:testid>/create_questions/',General.create_questions, name = "create_questions"),
    path('geturl/<int:testid>', General.geturl, name = "geturl"),
    path('start_a_test/<int:testid>', General.start_a_test, name = "start_a_test"),
    path('start_a_test/<int:testid>/take_test/<int:current_question_num>', General.take_test, name = "take_test"),
    path('login/', General.login_form, name = "login_form"),
    path('register/', General.register, name = "register"),
    path('log_out/', General.log_out, name = "log_out"),
    path('statistics/', General.statistics, name = "statistics"),
    path('access_denied/', General.access_denied, name = "access_denied"),
    path('show_my_profile/', General.show_my_profile, name = "show_my_profile"),
    path('show_change_user_credentials/', General.show_change_user_credentials, name = "show_change_user_credentials"),
    path('storage/test_list', TestList.as_view(), name = "test_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
