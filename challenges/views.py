from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


monthly_challenges = {
    'january': 'Eat more protein entire month',
    'february': 'Sleep at least 7h every day',
    'march': 'Learn Django at least 15 minutes every day',
    'april': 'Eat more protein entire month',
    'may': 'Sleep at least 7h every day',
    'june': 'Learn Django at least 15 minutes every day',
    'july': 'Eat more protein entire month',
    'august': 'Sleep at least 7h every day',
    'september': 'Learn Django at least 15 minutes every day',
    'october': 'Eat more protein entire month',
    'november': 'Sleep at least 7h every day',
    'december': 'Learn Django at least 15 minutes every day',
}
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
