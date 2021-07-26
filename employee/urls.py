from django.urls import path
from . import views

urlpatterns = [
    path("",views.EmployeeView.as_view(),name="employee"),
    path("add-accident",views.CreateAccidentView.as_view(),name="add-accident"),
    path("<slug:slug>",views.EmployeeInfoView.as_view(),name="employee-info"),
]
