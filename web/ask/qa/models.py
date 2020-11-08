from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class QuestionManager(models.Manager):
    def recent(self):
        return self.get_queryset().order_by('-id')

    def popular(self):
        return self.get_queryset().order_by('-rating')

    def __str__(self):
        return self.text


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='question_to_users')

    objects = QuestionManager()

    def get_url(self):
        return reverse('show_question', kwargs={'question_id': self.pk})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
