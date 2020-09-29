# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from core.constants import close_status, open_status, Open, Close


class Question(models.Model):
    title = models.CharField(max_length=255)
    question = models.TextField()
    status = models.CharField(max_length=10, choices=[(open_status, Open), (close_status, Close)], default=open_status)
    vote = models.IntegerField()
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return '{}'.format(self.title)


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer = models.TextField()
    vote = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return '{}'.format(self.name)
