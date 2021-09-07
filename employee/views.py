from django.http.response import HttpResponseRedirect
from .models import Accident, Employee, Refuel, VehicleBreakdown
from vehicle.models import Vehicle
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import AccidentForm,RefuelForm, VehicleBreakdownForm
from django.views.generic import DetailView,ListView,UpdateView
from django.urls import reverse



# Create your views here.


class EmployeeView(View):

    @method_decorator(login_required(login_url='/'))
    def get(self, request):
        user = request.user
        employee_slug = request.session.get('employee_slug')
        vehicle_slug = request.session.get('employee_vehicle')

        if vehicle_slug is None:
            try :
                vehicle = Vehicle.objects.get(employee=request.session.get('employee_id'))
                vehicle_slug = vehicle.slug
                request.session['employee_vehicle'] = vehicle_slug
            except:
                pass
        
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


        def get_context_data(self, **kwargs):
            ctx = super().get_context_data(**kwargs)
            employee = self.request.session.get('employee_id')
            try:
                ctx['refuels'] = Refuel.objects.get(employee=employee)
                return ctx
            except:
                ctx['refuels'] = None
                return ctx
            

class AddVehicleBreakdown(View):
    def get(self, request, *args, **kwargs):
        form = VehicleBreakdownForm()

        return render(request,"employee/add_vehicle_breakdown.html",{
            "form":form,
        })

    def post(self, request, *args, **kwargs):
        form = VehicleBreakdownForm(request.POST)
        employee = request.session.get('employee_id')
        vehicle = request.session.get('employee_vehicle_id')

        if form.is_valid():
            form_new = form.save(commit=False)
            form_new.employee = Employee.objects.get(pk=employee)
            form_new.vehicle = Vehicle.objects.get(pk=vehicle)
            form_new.save()
            return HttpResponseRedirect(reverse('all-breakdowns'))

        return render(request,"employee/add_vehicle_breakdown.html",{
            "form":form
        })
        
class VehicleBreakdowns(ListView):
        template_name = "employee/vehicle_breakdowns.html"
        model = VehicleBreakdown
        context_object_name = "breakdowns"


        def get_context_data(self, **kwargs):
            ctx = super().get_context_data(**kwargs)
            vehicle = self.request.session.get('employee_vehicle_id')
            
            try:
                ctx['breakdowns'] = Vehicle.objects.get(pk=vehicle).vehicle_breakdowns.all()
                return ctx
            except:
                ctx['breakdowns'] = None
                return ctx


class EmployeeEdit(UpdateView):
    model = Employee
    fields = ['address','contact','categories']
    template_name = 'employee/employee_edit.html'
    