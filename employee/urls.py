from django.urls import path
from . import views

urlpatterns = [
    path("",views.EmployeeView.as_view(),name="employee"),
    path("<slug:slug>",views.EmployeeInfoView.as_view(),name="employee-info")
]
