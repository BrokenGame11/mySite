# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Game(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField()

    def __unicode__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()
    game = models.ManyToManyField(Game)

    def __unicode__(self):
        return self.title


# Create your models here.
