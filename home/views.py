from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    # Page from the theme
    return render(request, "pages/index.html")


def health_check(request):
    return "ok"
