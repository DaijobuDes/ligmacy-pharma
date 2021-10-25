from django import forms
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from .models import *

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = '__all__'

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
