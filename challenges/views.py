from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    if month == 'january':
        challenge_text = 'Eat more protein entire month'
    elif month == 'february':
        challenge_text = 'Sleep at least 7h every day'
    elif month == 'march':
        challenge_text = 'Learn Django at least 15 minutes every day'
    else:
        return HttpResponseNotFound('This month is not supported!')
    return HttpResponse(challenge_text)
