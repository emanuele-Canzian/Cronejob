from django.shortcuts import render

# views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, World!')
