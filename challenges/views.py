from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    'december': 'Learn Django at least 15 minutes every day',
}
# Create your views here.

# def index(request):
#     months = list(monthly_challenges.keys())
#     links = ""

    # for month in months:
    #     month_url = reverse('month-challenge', args=[month])
    #     links = links + f"<a href='{month_url}'>{month}</a></br>"
    #
    # return HttpResponse(links)

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())


    for month in months:
        month_path = reverse("month-challenge", args=[month])
        capitalized_month = month.capitalize()
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

# allows give as parameter pure number instead of name of the month in url statament
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    try:
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound('Page not found!')

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('This month is not supported!')


