"""tester URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('univ_app.urls')),
    path('create/', include('univ_app.urls')),
    path('testme/', include('univ_app.urls')),
    path('sign/', include('univ_app.urls')),
    path('stat/', include('univ_app.urls')),
    # path('createtest/<int:testid>/create_questions/', include('univ_app.urls')),

    # path('createtest/<int:testid>/create_questions/', include('univ_app.urls')),
    # path('add_answer', include('univ_app.urls')),
]
