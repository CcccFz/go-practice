# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def index(request):
    return HttpResponse(u"欢迎光临!")

def main(request):
    return render(request, 'blog/main.html')

def add(request):
    x = request.GET['x']
    y = request.GET['y']
    result = int(x) + int(y)
    return HttpResponse(str(result))

def sum(request, x, y):
    result = int(x) + int(y)
    return HttpResponse(str(result*10))

def old(request):
    return HttpResponseRedirect(
        reverse('new')
    )

def new(request):
    return render(request, 'blog/new.html')

def home(request):
    return render(request, 'blog/home.html', {'lst': range(50)})
