from django.contrib import admin
import datetime
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table, TableStyle,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from vehicle.models import Category

# Register your models here.
from .models import Brand,Category,Vehicle,Fuel,InsuranceCompany,InsurancePolicy

@admin.action(description='Export to PDF')
def export_to_pdf(self,request,queryset):
    width,height =A4
    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=A4,bottomup=2)
    if request.GET:
        dic_list = list(request.GET.keys())
        f = dic_list[0]
        fi = f.split("_")[0]
        if fi == 'category':
            id = request.GET[dic_list[0]]
            cat = Category.objects.get(pk=id).category_name
            c.drawString(455,20,f"Filtered by: {fi} ({cat})")
        elif fi == 'brand':
            id = request.GET[dic_list[0]]
            bra = Brand.objects.get(pk=id).name
            c.drawString(455,20,f"Filtered by: {fi} ({bra})")\

    c.setTitle('Vehicles')
    styles = getSampleStyleSheet()
    styleH = styles['Heading1']
    p = Paragraph("Vehicles",styleH)
    w,h = p.wrapOn(c,100,10)
    p.drawOn(c,40,719)
    c.drawCentredString(500,750,'Vozni Park @Company')
    c.drawCentredString(500,720,str(datetime.datetime.now().strftime("%d %B, %Y")))
    data = [['Model','Category','Brand','Fuel','Year']]

    for vehicle in queryset:
        list_emp_data = [vehicle.model_name,vehicle.category,vehicle.brand,vehicle.fuel,vehicle.year]
        data.append(list_emp_data)

    rows = len(data)
    cal = 20 + rows*27
    table = Table(data,spaceBefore=5)
    style = TableStyle([
    ('BACKGROUND', (0,0), (4,0), colors.purple),
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

    return FileResponse(buf,as_attachment=True,filename='vehicles.pdf')

class BrandAdmin(admin.ModelAdmin):
    list_display = ("name","country",)
    ordering = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)
    ordering = ['category_name']


class VehicleAdmin(admin.ModelAdmin):
    list_display = ("model_name","category","brand",)
    list_filter = ("category","brand",'fuel')
    prepopulated_fields = {"slug":("model_name","license_plate",)}
    actions = [export_to_pdf]

class FuelAdmin(admin.ModelAdmin):
    list_display = ("type",)
    ordering = ['type']

class InsuranceCompanyAdmin(admin.ModelAdmin):
    list_display = ("name",)

class InsurancePolicyAdmin(admin.ModelAdmin):
    list_display = ("insurance_company","vehicle",)
    list_filter = ('insurance_expires',)

admin.site.register(Brand,BrandAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(Fuel,FuelAdmin)
admin.site.register(InsuranceCompany,InsuranceCompanyAdmin)
admin.site.register(InsurancePolicy,InsurancePolicyAdmin)


admin.site.site_header = "Administracija Voznog Parka"
admin.site.index_title = "Vozni Park"
admin.site.site_title = "ADMIN"

