# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, auth
from django_comments.models import Comment
from django.views.decorators.csrf import csrf_exempt
from .models import Category, BBS, BBSUser

# Create your views here.

def index(request):
    bbs_list = BBS.objects.all()
    bbs_categories = Category.objects.all()
    return render_to_response('bbs/index.html', {'bbs_list': bbs_list, 'user': request.user, 'bbs_category': bbs_categories, 'cata_id': 0})

def category(request, cata_id):
    bbs_list = BBS.objects.filter(category__id=cata_id)
    bbs_categories = Category.objects.all()
    return render_to_response('bbs/index.html',
                               {'bbs_list': bbs_list,
                                'user': request.user,
                                'bbs_category': bbs_categories,
                                'cata_id': int(cata_id),
                              })

def detail(request, bid):
    bbs = BBS.objects.get(id=bid)
    bbs_categories = Category.objects.all()
    return render_to_response('bbs/detail.html', {'bbs_obj': bbs, 'user': request.user, 'bbs_category': bbs_categories, 'cata_id': bbs.category_id})

@csrf_exempt
def sub_comment(request):
    bbs_id = request.POST.get('bbs_id')
    comment = request.POST.get('comment_content')

    Comment.objects.create(
        content_type_id=9,
        object_pk=bbs_id,
        site_id=1,
        user=request.user,
        comment=comment,
    )
    return HttpResponseRedirect('/bbs/detail/%s' % bbs_id)

def pub_bbs(request):
    bbs_categories = Category.objects.all()
    return render_to_response('bbs/pub_bbs.html', {'bbs_category': bbs_categories})

@csrf_exempt
def sub_bbs(request):
    content=  request.POST.get('content')
    author = BBSUser.objects.get(user__username=request.user)
    BBS.objects.create(
        title = request.POST.get('title'),
        summary = request.POST.get('summary'),
        content = content,
        author = author,
        view_count = 1,
        ranking = 1,
    )

    return HttpResponseRedirect('/bbs')

def login_bbs(request):
    return render_to_response('bbs/login.html')

@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user is not None:  # and user.is_active:
        # correct password and user is marked "active"
        auth.login(request, user)
        content = '''
        Welcome %s !!!

        <a href='/logout/' >Logout</a>

         ''' % user.username
        # return HttpResponse(content)
        return HttpResponseRedirect('/')
    else:
        return render_to_response('bbs/login.html', {'login_err': 'Wrong username or password!'})

def logout_bbs(request):
    user = request.user
    auth.logout(request)
    return HttpResponse("<b>%s</b> logged out! <br/><a href='/index/'>Re-login</a>" % user)
