from django.forms import ModelForm
from carmanager.models import Car

__author__ = 'zhila'

class CarForm(ModelForm):
    class Meta:
        model = Car