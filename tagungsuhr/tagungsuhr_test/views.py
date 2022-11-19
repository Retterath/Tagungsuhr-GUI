from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def index(request):  # Get the HTTP request from a user
    return render(request, "home/index.html")

def tagungsuhr_test(request):
    return render(request, "home/tagungsuhr_test.html")

def extra(request):  # Get the HTTP request from a user
    now = datetime.now()
    return render(request, "home/extra.html", {
        "newyear": now.month == 1 and now.day == 1
    })