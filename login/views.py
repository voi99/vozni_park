from employee.models import Employee
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate,login, logout
from .forms import LoginForm

# Create your views here.

class ChooseLoginView(View):
    def get(self, request):
        return render(request,"login/choose_login.html")


def login_view(request):
    form = LoginForm(request.POST or None)
    w_pass =""
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            emp = Employee.objects.get(user=user)
            request.session['employee_id'] = emp.id
            request.session['employee_slug'] = emp.slug
            try:
                request.session['employee_vehicle_id'] = emp.vehicle.id
                request.session['employee_vehicle'] = emp.vehicle.slug
            except:
                request.session['employee_vehicle_id'] = None

            return redirect('employee')
        else:
           w_pass = "Wrong Password!"

    return render(request,"login/login.html",{"form":form,"w_pass":w_pass})

def logout_view(request):
    logout(request)
    return redirect("/")
