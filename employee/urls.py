from django.urls import path
from . import views

urlpatterns = [
    path("",views.EmployeeView.as_view(),name="employee"),
    path("add-accident",views.CreateAccidentView.as_view(),name="add-accident"),
    path("add-breakdown",views.AddVehicleBreakdown.as_view(),name="add-breakdown"),
    path("refuel",views.AddReful.as_view(),name='refuel'),
    path("refuels/all",views.RefuelsView.as_view(),name='all-refuels'),
    path("<slug:slug>",views.EmployeeInfoView.as_view(),name="employee-info"),
    path("accident/<int:pk>",views.AccidentView.as_view(),name='accident'),
]
