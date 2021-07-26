from django.db.models import fields
from django.forms import ModelForm
from .models import Accident

class AccidentForm(ModelForm):
    class Meta:
        model = Accident
        fields = '__all__'