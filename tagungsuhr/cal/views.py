from django.shortcuts import render
from django.http import HttpRequest
import datetime as dt
from django import forms
# Create your views here.

days = [dt.datetime.now(), dt.datetime.today() + dt.timedelta(days=1)]
json = []

class NewCalForm(forms.Form):
    date_from_form = forms.DateField(label="Neues Datum")
    text = forms.CharField()

def index(request):
    return render(request, "cal/index.html", {
        "days" : days
    })

def add(request):
    if request.method == "POST":  
        form = NewCalForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date_from_form']  # All submited userdata. Name in [] comes from NewCalForm
            days.append(date)
    else:
        form = NewCalForm(request.GET)
    return render(request, "cal/add.html", {
        "form": NewCalForm()
    })