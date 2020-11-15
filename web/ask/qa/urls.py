from django.urls import path

from qa import views

urlpatterns = [
    path('<int:question_id>/', views.show_question, name='show_question')
]
