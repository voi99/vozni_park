from django.contrib.auth import login
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.


class EmployeeView(View):

    @method_decorator(login_required(login_url='/'))
    def get(self, request):
        user = request.user
        return render(request,"employee/employee.html",{
            "user":user
        })

class UserView(View):
    pass