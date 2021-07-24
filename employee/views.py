from django.shortcuts import render
from django.views import View

# Create your views here.

class EmployeeView(View):
    def get(self, request):
        return render(request,"employee/employee.html")