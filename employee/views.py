from employee.models import Employee
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.


class EmployeeView(View):

    @method_decorator(login_required(login_url='/'))
    def get(self, request):
        user = request.user
        employee_slug = request.session.get('employee_slug')
       
        return render(request,"employee/employee.html",{
            "user":user,
            "employee_slug":employee_slug
        })

class EmployeeInfoView(View):
    def get(self,request,slug):
        employee = Employee.objects.get(slug=slug)
        print(employee)
        return render(request,"employee/employee-info.html",{
            "employee":employee
        })
