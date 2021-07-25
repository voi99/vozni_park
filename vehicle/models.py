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


class Vehicle(models.Model):
    model_name = models.CharField(max_length=50)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, related_name="category_vehicles")
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,related_name="brand_vehicles")
    year = models.IntegerField(validators=[MinValueValidator(2000),
    MaxValueValidator(datetime.datetime.now().year)])
    color = models.CharField(max_length=50)
    last_registration = models.DateField()
    slug = models.SlugField(default="",null=False,db_index=True)
    garage = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['garage'],zoom=7)

    # def save(self,*args, **kwargs):
    #     self.slug = slugify(self.model_name)
    #     super().save()
    
    def __str__(self):
        return f"{self.model_name} ({self.category}) - {self.brand}"
     