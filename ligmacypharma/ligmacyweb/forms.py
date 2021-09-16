from django import forms
from .models import *

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = '__all__'

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
