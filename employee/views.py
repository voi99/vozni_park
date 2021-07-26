from .models import Employee,Accident
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import AccidentForm
from django import forms


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



class CreateAccidentView(View):
    def get(self, request, *args, **kwargs):
        form = AccidentForm()
        employee = self.request.session.get('employee_id')
        vehicle = self.request.session.get('employee_vehicle_id')
        form.fields['employee'].initial = employee
        form.fields['employee'].disabled = True
        form.fields['vehicle'].initial = vehicle
        form.fields['vehicle'].disabled = True

        return render(request,"employee/create_accident.html",{
            "form":form,
            "employee":employee,
            "vehicle":vehicle
        })

    def post(self, request, *args, **kwargs):
        form = AccidentForm(request.POST,request.FILES)
        employee = self.request.session.get('employee_id')
        vehicle = self.request.session.get('employee_vehicle_id')
        form.fields['employee'].initial = employee
        form.fields['employee'].disabled = True
        form.fields['vehicle'].initial = vehicle
        form.fields['vehicle'].disabled = True
        
        if form.is_valid():
            form.save()
            return redirect('/employee')
        
        return render(request,"employee/create_accident.html",{
            "form":form
        })