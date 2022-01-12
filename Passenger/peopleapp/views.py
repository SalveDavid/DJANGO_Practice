from django.shortcuts import render
from .models import Passenger


def passengersdata(request):
    passengers = Passenger.objects.all()
    empDict = {'passengers': passengers}
    return render(request, 'peopleapp/passengers.html', empDict)
