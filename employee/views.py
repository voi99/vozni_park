from django.http.response import HttpResponseRedirect
from .models import Accident, Employee, Refuel
from vehicle.models import Vehicle
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import AccidentForm,RefuelForm
from django.views.generic import DetailView,ListView
from django.urls import reverse



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

        return render(request,"employee/create_accident.html",{
            "form":form,
        })

    def post(self, request, *args, **kwargs):
        form = AccidentForm(request.POST,request.FILES)
        employee = request.session.get('employee_id')
        vehicle = request.session.get('employee_vehicle_id')
        
        if form.is_valid():
            form_new = form.save(commit=False)
            form_new.employee = Employee.objects.get(pk=employee)
            form_new.vehicle = Vehicle.objects.get(pk=vehicle)
            form_new.save()
            return redirect(f"accident/{form_new.pk}")

        return render(request,"employee/create_accident.html",{
            "form":form
        })

class AccidentView(DetailView):
        template_name = "employee/accident.html"
        model = Accident

class AddReful(View):
    def get(self, request, *args, **kwargs):
        form = RefuelForm()

        return render(request,"employee/add_refuel.html",{
            "form":form,
        })

    def post(self, request, *args, **kwargs):
        form = RefuelForm(request.POST)
        employee = request.session.get('employee_id')
        vehicle = request.session.get('employee_vehicle_id')
        print(employee)

        if form.is_valid():
            form_new = form.save(commit=False)
            form_new.employee = Employee.objects.get(pk=employee)
            form_new.vehicle = Vehicle.objects.get(pk=vehicle)
            form_new.save()
            return HttpResponseRedirect(reverse('all-refuels'))

        return render(request,"employee/add_fuel.html",{
            "form":form
        })

class RefuelsView(ListView):
        template_name = "employee/refuels.html"
        model = Refuel
        context_object_name = "refuels"
        