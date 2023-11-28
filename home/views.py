from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


def index(request):
    # Page from the theme
    return render(request, "pages/index.html")


@api_view(("GET",))
def health_check(request):
    return Response("ok", status=status.HTTP_200_OK)
