from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='tests', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created', ]

    def __str__(self):
        return self.name


class Question(models.Model):
    no = models.IntegerField(default=0)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)

    class Meta:
        ordering = ['test', 'no']

    def __str__(self):
        return self.name


class Choice(models.Model):
    no = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)

    class Meta:
        ordering = ['question', 'no']

    def __str__(self):
        return self.name
