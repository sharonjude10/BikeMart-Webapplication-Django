from django.urls import path

from . import views

urlpatterns = [ 

            path ('bikes/', views.bikes, name="scooters"),
            path ('bikes/', views.bikes, name="bikes")

]