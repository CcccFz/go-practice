# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BBS, Category, BBSUser


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'administrator')

class BBSAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary', 'category', 'author', 'signature', 'view_count', 'ranking', 'created_at', 'updated_at')
    list_filter = ('author', 'view_count', 'ranking', 'created_at')
    search_fields = ('title', 'author__user__username')

    def signature(self, obj):
        return obj.author.signature
    signature.short_description = 'short_signature'


class BBSUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'signature', 'photo')

admin.site.register(BBS, BBSAdmin) # 把自定义的类绑定到注册的类中
admin.site.register(Category, CategoryAdmin)  # 把自定义的类绑定到注册的类中
admin.site.register(BBSUser, BBSUserAdmin)

