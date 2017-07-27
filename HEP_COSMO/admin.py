from django.contrib import admin
from .models import *

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    '''
        Admin View for Article
    '''
    list_display = ('year','index',  'people', 'title', 'arxiv', 'journal', 'published_date')
    list_display_links = ('people', 'title',)
    search_fields = ('year', 'title', 'people')
    list_per_page = 25

admin.site.register(Article, ArticleAdmin)


class PeopleAdmin(admin.ModelAdmin):
    '''
        Admin View for People
    '''
    list_display = ('position', 'index', 'name', 'email', 'location', 'link')
    list_display_links = ('name',)
    search_fields = ('position', 'name')

admin.site.register(People, PeopleAdmin)


class SeminarAdmin(admin.ModelAdmin):
    '''
        Admin View for Seminar
    '''
    list_display = ('date_start','date_end','place', 'title', 'lecturer', 'published_date')
    list_display_links = ('date_start', 'date_end', 'place', 'title')
    list_filter = ('date_start',)
    search_fields = ('title', 'lecturer')

admin.site.register(Seminar, SeminarAdmin)

