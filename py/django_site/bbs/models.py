# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

# Create your models here.

@python_2_unicode_compatible
class BBS(models.Model):
    title = models.CharField(max_length=64)
    summary = models.CharField(max_length=256, blank=True)
    content = models.TextField()
    category = models.ForeignKey('Category')
    author = models.ForeignKey('BBSUser')
    view_count = models.IntegerField()
    ranking = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    administrator = models.ForeignKey('BBSUser')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class BBSUser(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128, default='This guy is too lazy.')
    photo = models.ImageField(upload_to="imgs", default="imgs/mm.jpg")

    def __str__(self):
        return self.user.username
