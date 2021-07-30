from django.contrib import admin
from .models import Accident,Refuel,Employee,VehicleBreakdown
import datetime
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib.units import inch


# Register your models here.

@admin.action(description='Export to PDF')
def export_to_pdf(self,request,queryset):
    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=letter)
    data = [['First Name','Last Name','Address','Contact']]

    for employee in queryset:
        list_emp_data = [employee.first_name,employee.last_name,employee.address,employee.contact]
        data.append(list_emp_data)

    table = Table(data)
    style = TableStyle([
    ('BACKGROUND', (0,0), (3,0), colors.purple),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke), # The negative one means "go to the last element"
    
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    
    ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 14),
    
    ('BOTTOMPADDING', (0,0), (-1,0), 12), # 12 = 12 pixels
    
    ('BACKGROUND', (0,1), (-1,-1), colors.beige), # Background for the rest of the table (excluding the title row)
    ])
    table.setStyle(style)
    table.wrapOn(c,400,100)
    table.drawOn(c,150,700)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename='employees.pdf')


class EmployeeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("first_name","last_name",)}
    list_display = ("first_name","last_name","vehicle",)
    list_filter = ("categories",)
    actions = [export_to_pdf]

class AccidentAdmin(admin.ModelAdmin):
    list_display = ("employee","vehicle","date",)

class RefuelAdmin(admin.ModelAdmin):
    list_display = ("employee","vehicle","date",)

class VehicleBreakdownAdmin(admin.ModelAdmin):
    list_display = ("vehicle","title","date",)


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Accident,AccidentAdmin)
admin.site.register(Refuel,RefuelAdmin)
admin.site.register(VehicleBreakdown,VehicleBreakdownAdmin)
