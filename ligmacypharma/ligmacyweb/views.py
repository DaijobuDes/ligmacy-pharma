from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
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

    def post(self, request):
        form = SignUpForm(request.POST)
        email = request.POST.get("email")
        password = request.POST.get("password")
        name = request.POST.get("name")
        age = request.POST.get("age")
        form = SignUp(email = email, password = password,name = name, age = age)
        form.save()
        return redirect("ligmacyweb:sign_up")

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
        medicine_name = request.POST.get("med_name")
        price = request.POST.get("price")
        stock = request.POST.get("stock")
        form = Medicine(name = medicine_name, price = price, stock = stock)
        form.save()
        return redirect("ligmacyweb:add_medicine")
    
    def get(self,request):
        return render(request, "add_record.html")