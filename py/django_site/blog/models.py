# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Sex(models.Model):
    sex = models.CharField(max_length=8, default='male')

    def __str__(self):
        # 在Python2中使用 def __unicode__(self):
        return self.sex


@python_2_unicode_compatible
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    salary = models.IntegerField()
    sex = models.ForeignKey('Sex')

    def my_property(self):
        return self.salary * 0.8

    my_property.short_description = "After Salary"
    after_salary = property(my_property)

    def __str__(self):
        # 在Python2中使用 def __unicode__(self):
        return '%s %d %d %s' % (self.name, self.age, self.salary, self.sex)
