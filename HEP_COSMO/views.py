from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'HEP/index.html', {})

def members(request):
    return render(request, 'HEP/members.html', {})