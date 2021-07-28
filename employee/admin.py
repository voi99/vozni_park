from django.contrib import admin
from .models import Accident,Refuel,Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("first_name","last_name",)}
    list_display = ("first_name","last_name","vehicle",)
    list_filter = ("categories",)

class AccidentAdmin(admin.ModelAdmin):
    list_display = ("employee","vehicle","date",)

class RefuelAdmin(admin.ModelAdmin):
    list_display = ("employee","vehicle","date",)


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Accident,AccidentAdmin)
admin.site.register(Refuel,RefuelAdmin)
