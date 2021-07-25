from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>",views.VehicleInfo.as_view(),name="vehicle")
]