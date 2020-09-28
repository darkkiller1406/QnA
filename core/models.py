# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    question = models.TextField()
    status = models.BooleanField(choices=[(True, 'Open'), (False, 'Close')], default=True)
    vote = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.title)


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer = models.TextField()
    vote = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    questions = models.ManyToManyField('Question', blank=True)