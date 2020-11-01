from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class QuestionManager(models.Manager):
    def recent(self):
        return self.get_queryset().order_by('-added_at')

    def popular(self):
        return self.get_queryset().order_by('-rating')

    def __str__(self):
        return self.text


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_to_users')

    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
