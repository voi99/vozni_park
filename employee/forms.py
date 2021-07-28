from django import forms
from django.forms import ModelForm
from .models import Accident, Refuel
import datetime
from bootstrap_datepicker_plus import DatePickerInput

class AccidentForm(ModelForm):
    class Meta:
        model = Accident
        exclude = ['employee','vehicle']
        widgets= {'date':forms.SelectDateWidget(years=[datetime.datetime.now().year])}

class RefuelForm(ModelForm):
    class Meta:
        model = Refuel
        exclude = ['employee','vehicle']
        widgets= {'date':DatePickerInput(format='%Y-%m-%d')}
        labels={'amount':'Amount(€)'}
