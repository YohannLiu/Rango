# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Yohann.models import Category, Page
from Yohann.models import UserProfile

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class PageAdmin(admin.ModelAdmin):
    # To display individual fields
    list_display = ('title', 'category', 'url')
    # prepopulated_fields = {'slug': ('title',)}

admin.site.register(UserProfile)
admin.site.register(Page,PageAdmin)