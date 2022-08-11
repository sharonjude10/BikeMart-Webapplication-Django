from django.urls import path

from . import views

urlpatterns = [ 

            path ('bikes/scooter', views.scooters, name="scooters"),
            path ('bikes/', views.bikes, name="bikes"),
            

]