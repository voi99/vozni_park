from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
from vehicle.models import Vehicle

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    categories = models.ManyToManyField('vehicle.Category')
    vehicle = models.OneToOneField('vehicle.Vehicle',on_delete=CASCADE,null=True)
    slug = models.SlugField(default="",null=False,db_index=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "

class Accident(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="employee_accidents")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="vehicle_accidents")
    city = models.CharField(max_length=100)
    location = PlainLocationField(zoom=7)
    image = models.ImageField(upload_to='images')
    date = models.DateField()
    
    def __str__(self):
        return f"{self.city} {self.date} - {self.vehicle}"

