from django.contrib import admin
from .models import Accident,Refuel,Employee,VehicleBreakdown
import datetime
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from vehicle.models import Category



# Register your models here.

@admin.action(description='Export to PDF')
def export_to_pdf(self,request,queryset):
    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=letter)
    if request.GET:
        dic_list = list(request.GET.keys())
        f = dic_list[0]
        fi = f.split("_")[0]
        if fi == 'categories':
            id = request.GET[dic_list[0]]
            cat = Category.objects.get(pk=id).category_name
            c.drawString(455,20,f"Filtered by: {fi} ({cat})")
    c.setTitle('Employees')
    styles = getSampleStyleSheet()
    styleH = styles['Heading1']
    p = Paragraph("Employees",styleH)
    w,h = p.wrapOn(c,100,10)
    p.drawOn(c,40,719)
    c.drawCentredString(500,750,'Vozni Park @Company')
    c.drawCentredString(500,720,str(datetime.datetime.now().strftime("%d %B, %Y")))
    data = [['First Name','Last Name','Address','Contact']]

    for employee in queryset:
        list_emp_data = [employee.first_name,employee.last_name,employee.address,employee.contact]
        data.append(list_emp_data)

    rows = len(data)
    cal = rows*27
    table = Table(data)
    style = TableStyle([
    ('BACKGROUND', (0,0), (3,0), colors.purple),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke), 
    
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    
    ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 14),
    
    ('BOTTOMPADDING', (0,0), (-1,0), 12), 
    ('RIGHTPADDING', (0,0), (-1,0), 31), 
    ('LEFTPADDING', (0,0), (-1,0), 31), 
    
    ('BACKGROUND', (0,1), (-1,-1), colors.beige), 
    ])
    table.setStyle(style)
    table.wrapOn(c,400,100)
    table.drawOn(c,40,750-cal)
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
    list_filter = ("date",)

class VehicleBreakdownAdmin(admin.ModelAdmin):
    list_display = ("vehicle","title","date",)


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Accident,AccidentAdmin)
admin.site.register(Refuel,RefuelAdmin)
admin.site.register(VehicleBreakdown,VehicleBreakdownAdmin)
