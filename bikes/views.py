from django.shortcuts import render

from .models import Destination
from .  import views

# Create your views here.
def bikes(request):
    dests=Destination.objects.all()
    return render(request, 'bikes.html', {'dests': dests})




