from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Flight
# Create your views here.
def index(request):
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "flights/index.html", context)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id) # pk = primary key
    except Flight.DoesNotExist: 
        raise Http404("Flight does not exist")
    context = {
        "id": flight.id,
        "origin": flight.origin,
        "dest": flight.destination,
        "duration": flight.duration
    }
    return render(request,"flights/flight.html", context)