"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path

import qa.views

urlpatterns = [
    path('', qa.views.list_recent_questions, name='list_recent_questions'),
    path('login/', qa.views.signin, name='signin'),
    path('signup/', qa.views.signup, name='signup'),
    path('question/', include('qa.urls')),
    path('ask/', qa.views.add_question, name='ask'),
    path('popular/', qa.views.list_popular_questions, name='list_popular_questions'),
    path('new/', qa.views.test),
    path('admin/', admin.site.urls),
]
