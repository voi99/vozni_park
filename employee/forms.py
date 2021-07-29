from django import forms
from django.forms import ModelForm
from .models import Accident, Refuel, VehicleBreakdown
import datetime
from bootstrap_datepicker_plus import DatePickerInput

class AccidentForm(ModelForm):
    class Meta:
        model = Accident
        exclude = ['employee','vehicle']
        widgets=  {'date':DatePickerInput(format='%Y-%m-%d')}
        
class RefuelForm(ModelForm):
    class Meta:
        model = Refuel
        exclude = ['employee','vehicle']
        widgets= {'date':DatePickerInput(format='%Y-%m-%d')}
        labels={'amount':'Amount(€)'}

class VehicleBreakdownForm(ModelForm):
    class Meta:
        model = VehicleBreakdown
        exclude = ['employee','vehicle']
        widgets= {'date':DatePickerInput(format='%Y-%m-%d')}

