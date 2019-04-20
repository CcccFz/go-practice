# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Person

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'sex', 'salary', 'after_salary')

admin.site.register(Person, PersonAdmin)
