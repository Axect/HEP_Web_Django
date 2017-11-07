from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^index', views.home, name='index'),
    url(r'^members', views.members, name='members'),
    url(r'^publish', views.publish, name='publish'),
    url(r'^research', views.research, name='research'),
    url(r'^calendar', views.calendar, name='calendar'),
    url(r'^seminar', views.seminar, name='seminar'),
    url(r'^finedust', views.finedust, name='finedust'),
    url(r'^link', views.link, name='link'),
    url(r'^arxiv', views.arxiv, name='arxiv'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^contact', views.snail, name='snail'),
]
