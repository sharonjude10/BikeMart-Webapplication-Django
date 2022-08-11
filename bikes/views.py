from django.shortcuts import render

from .models import Destination
from .  import views

# Create your views here.
def bikes(request):
    dests=Destination.objects.filter(category="Bike")
    return render(request, 'bikes.html', {'dests': dests})




def scooters(request):
    dests=Destination.objects.filter(category="Scooter")
    return render(request, 'scooter.html', {'dests': dests})


def details(request):
    return render(request,'details.html')

