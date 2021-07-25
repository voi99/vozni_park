from django.shortcuts import render
from django.views import View
from .models import Vehicle
# Create your views here.

class VehicleInfo(View):
    def get(self,request,slug):
        vehicle = Vehicle.objects.get(slug=slug)
        vehicle_cor1 = vehicle.location.split(",")[0]
        vehicle_cor2 = vehicle.location.split(",")[1]


        return render(request,"vehicle/vehicle.html",{
            "vehicle":vehicle,
            "vehicle_cor1":vehicle_cor1,
            "vehicle_cor2":vehicle_cor2
        })