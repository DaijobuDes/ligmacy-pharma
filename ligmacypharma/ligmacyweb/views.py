from django.shortcuts import render
from django.views.generic import View
from .forms import *

# Create your views here.

class IndexView(View):
    
    def __init__(self):
        pass

    def get(self, request):
        return render(request, "index.html")


class AboutView(View):

    def __init__(self):
        pass

    def get(self, request):
        return render(request, "about.html")


class SignInView(View):

    def __init__(self):
        pass

    def get(self, request):
        return render(request, "sign_in.html")

class SignUpView(View):

    def __init__(self):
        pass

    def get(self, request):
        return render(request, "sign_up.html")

class DashboardView(View):
    def get(self,request):
        meds = Medicine.objects.all()
        accounts = SignUp.objects.all()
        context = {
            'med' : meds,
            'acc' : accounts
        }
        return render(request, 'dashboard.html', context)

class Add_MedicineView(View):
    def __init__(self):
        pass

    def post(self, request):
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine_name = request.POST.get("medicine_name")
            price = request.POST.get("price")
            stock = request.POST.get("stock")
            form = Medicine(name = medicine_name, price = price, stock = stock)
    
    def get(self,request):
        return render(request, "add_record.html")