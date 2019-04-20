"""django_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_view
from bbs import views as bbs_view

urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),

    # Blog url
    url(r'^$', blog_view.index),
    url(r'^main/$', blog_view.main, name='main'),
    url(r'^add/$', blog_view.add, name='add'),
    url(r'^sum/(\d+)/(\d+)/$', blog_view.sum, name='sum'),
    url(r'^old/$', blog_view.old, name='old'),
    url(r'^new/$', blog_view.new, name='new'),
    url(r'^home/$', blog_view.home, name='home'),

    # BBS url
    url(r'^bbs/$', bbs_view.index, name='index'),
    url(r'^bbs/category/(\d+)/$', bbs_view.category, name='category'),
    url(r'^bbs/detail/(\d+)/$', bbs_view.detail, name='detail'),
    url(r'^bbs/sub_comment/$', bbs_view.sub_comment, name='sub_comment'),
    url(r'^bbs/pub_bbs/$', bbs_view.pub_bbs, name='pub_bbs'),
    url(r'^bbs/sub_bbs/$', bbs_view.sub_bbs, name='sub_bbs'),
    url(r'^bbs/login_bbs/$', bbs_view.login_bbs, name='login_bbs'),
    url(r'^bbs/login/$', bbs_view.login, name='login'),
    url(r'^bbs/logout_bbs/$', bbs_view.logout_bbs, name='logout_bbs'),

]
