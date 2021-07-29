from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
import datetime
from location_field.models.plain import PlainLocationField



#from django.utils.text import slugify

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.country})"

class Category(models.Model):
    category_name = models.CharField(max_length=3)
    description = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.category_name}"

class Fuel(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type
    

class Vehicle(models.Model):
    model_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category_vehicles")
    brand = models.ForeignKey(Brand,on_delete=models.SET_NULL,null=True,related_name="brand_vehicles")
    fuel = models.ForeignKey(Fuel,on_delete=models.SET_NULL,null=True,related_name="fuel_vehicles")
    year = models.IntegerField(validators=[MinValueValidator(2000),
    MaxValueValidator(datetime.datetime.now().year)])
    color = models.CharField(max_length=50)
    slug = models.SlugField(default="",null=False,db_index=True)
    garage = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['garage'],zoom=100)

    # def save(self,*args, **kwargs):
    #     self.slug = slugify(self.model_name)
    #     super().save()
    
    def __str__(self):
        return f"{self.model_name}"

class InsuranceCompany(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Insurance companies"

class InsurancePolicy(models.Model):
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE, null=True, related_name="company_polices")
    vehicle = models.OneToOneField(Vehicle,on_delete=models.CASCADE,related_name='policy')
    policy_code = models.CharField(max_length=50)
    insurance_started = models.DateField()
    insurance_expires = models.DateField()

    class Meta:
        verbose_name_plural = "Insurance policies"

    def __str__(self):
        return f"{self.insurance_company} - {self.vehicle}"
    