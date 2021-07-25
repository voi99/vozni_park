from vehicle.models import Vehicle
from django.contrib import admin

# Register your models here.

from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("first_name","last_name",)}
    list_display = ("first_name","last_name","vehicle",)
    list_filter = ("categories",)


admin.site.register(Employee,EmployeeAdmin)
