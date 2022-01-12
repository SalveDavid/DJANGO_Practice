from django.shortcuts import render
from django.http import HttpResponse


def displayQuote(request):
    return HttpResponse("The best investment we can make is in yourself")
