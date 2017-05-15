from django.contrib import admin
from .models import *

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    '''
        Admin View for Article
    '''
    list_display = ('year', 'title', 'people', 'journal', 'author', 'published_date')
    list_display_links = ('title')
    search_fields = ('year', 'title', 'people')
    list_per_page = 25
    
admin.site.register(Article, ArticleAdmin)
