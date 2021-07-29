from django.urls import path
from . import views
from employee.views import VehicleBreakdowns

urlpatterns = [
    path("vehicle-breakdowns",VehicleBreakdowns.as_view(),name='all-breakdowns'),
    path("breakdowns/<int:pk>",views.VehicleBreakdownInfo.as_view(),name="vehicle-breakdown"),
    path("<slug:slug>",views.VehicleInfo.as_view(),name="vehicle"),
]
    