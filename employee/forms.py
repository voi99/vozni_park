from django import forms
from django.forms import ModelForm
from .models import Accident
import datetime

class AccidentForm(ModelForm):
    class Meta:
        model = Accident
        exclude = ['employee','vehicle']
        widgets= {'date':forms.SelectDateWidget(years=range(2000,datetime.datetime.now().year+1))}