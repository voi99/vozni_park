from django.contrib import admin

# Register your models here.
from .models import Brand,Category,Vehicle

class BrandAdmin(admin.ModelAdmin):
    list_display = ("name","country",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)

class VehicleAdmin(admin.ModelAdmin):
    list_display = ("model_name","category","brand",)
    list_filter = ("category",)

admin.site.register(Brand,BrandAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Vehicle,VehicleAdmin)

admin.site.site_header = "Administracija Voznog Parka"
admin.site.index_title = "Vozni Park"
admin.site.site_title = "ADMIN"

