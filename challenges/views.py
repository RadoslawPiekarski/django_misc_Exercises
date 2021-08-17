from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

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
    'december': None,
}


# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {"months": months})


# allows give as parameter pure number instead of name of the month in url statament
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    try:
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404()


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month_name': month,
        })
    except:
        raise Http404()
