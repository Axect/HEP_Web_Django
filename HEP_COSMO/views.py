from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(request, 'HEP/index.html', {})

def members(request):
    persons = People.objects.order_by('index')
    temp = []
    for person in persons:
        temp.append(person.position)
    positions = []
    [positions.append(position) for position in temp if position not in positions]
    return render(request, 'HEP/members.html', {'persons': persons, 'positions': positions})

def arxiv(request):
    return render(request, 'HEP/arxiv.html', {})

def calendar(request):
    return render(request, 'HEP/calendar.html', {})

def seminar(request):
    seminars = Seminar.objects.all().order_by('-date_start')
    for seminar in seminars:
        seminar.zipped = zip(seminar.ref.split(","), seminar.ref_link.split((",")))
    return render(request, 'HEP/seminar.html', {'seminars': seminars})

def snail(request):
    return render(request, 'HEP/snail.html', {})

def contact(request):
    return render(request, 'HEP/contact.html', {})

def finedust(request):
    return render(request, 'HEP/finedust.html', {})

def link(request):
    return render(request, 'HEP/link.html', {})

def research(request):
    return render(request, 'HEP/research.html', {})

def publish(request):
    articles = Article.objects.all().order_by('-index')
    persons = People.objects.all().order_by('-index')
    temp = []
    personlist = []
    [personlist.append(' ' + person.name) for person in persons]
    [personlist.append(person.name) for person in persons]
    for article in articles:
        temp.append(article.year)
    years = []
    [years.append(year) for year in temp if year not in years]
    return render(request, 'HEP/publish.html', {'articles': articles, 'yearlist': years, 'personlist': personlist})
