from django.shortcuts import render
from .models import Article

# Create your views here.

def index(request):
    return render(request, 'HEP/index.html', {})

def members(request):
    return render(request, 'HEP/members.html', {})

def arxiv(request):
    return render(request, 'HEP/arxiv.html', {})

def calendar(request):
    return render(request, 'HEP/calendar.html', {})

def contact(request):
    return render(request, 'HEP/contact.html', {})

def finedust(request):
    return render(request, 'HEP/finedust.html', {})

def link(request):
    return render(request, 'HEP/link.html', {})

def research(request):
    return render(request, 'HEP/research.html', {})

def publish(request):
    articles = Articles.objects.filter(index).order_by('index')
    return render(request, 'HEP/publish.html', {'articles': articles})