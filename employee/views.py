from .models import Employee,Accident
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView


# Create your views here.


class EmployeeView(View):

    @method_decorator(login_required(login_url='/'))
    def get(self, request):
        user = request.user
        employee_slug = request.session.get('employee_slug')
        vehicle_slug = request.session.get('employee_vehicle')
       
        return render(request,"employee/employee.html",{
            "user":user,
            "employee_slug":employee_slug,
            "vehicle_slug":vehicle_slug
        })

class EmployeeInfoView(View):
    @method_decorator(login_required(login_url='/'))
    def get(self,request,slug):
        employee = Employee.objects.get(slug=slug)
        vehicle_slug = request.session.get('employee_vehicle')
       
        
        return render(request,"employee/employee-info.html",{
            "employee":employee,
            "vehicle_slug":vehicle_slug
        })

class CreateAccidentView(CreateView):
    template_name = "employee/create_accident.html"
    model = Accident
    fields = "__all__"
    success_url = "/employee"