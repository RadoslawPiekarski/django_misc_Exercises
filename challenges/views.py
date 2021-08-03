from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse("Eat more protein entire month")

def february(request):
    return HttpResponse('Sleep at least 7h every day')
