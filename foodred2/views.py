# views.py
from django.shortcuts import render
from .models import Redfood
from django.urls import reverse


def index(request):
    dests=Redfood.objects.all()
    return render(request, "index.html", {'dests': dests})

