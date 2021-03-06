from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from location_field.models.plain import PlainLocationField
from vehicle.models import Vehicle
from django.urls import reverse

# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=10,validators=[RegexValidator(regex='^[0-9]{9,10}$')])
    categories = models.ManyToManyField('vehicle.Category')
    vehicle = models.OneToOneField('vehicle.Vehicle',on_delete=CASCADE,null=True,blank=True)
    slug = models.SlugField(default="",null=False,db_index=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "

    def get_absolute_url(self):
        return reverse('employee-info', kwargs={'slug': self.slug})

class Accident(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="employee_accidents")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="vehicle_accidents")
    city = models.CharField(max_length=100)
    location = PlainLocationField(based_fields=['city'],zoom=7)
    image = models.ImageField(upload_to='images')
    description = models.TextField(max_length=1000)
    date = models.DateField()
    
    def __str__(self):
        return f"{self.city} {self.date} - {self.vehicle}"

class Refuel(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="employee_refuels")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="vehicle_refuels")
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.date}  {self.amount}€"

class VehicleBreakdown(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="employee_vehicle_breakdowns")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="vehicle_breakdowns")
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return f"{self.vehicle} {self.title} ({self.date})"