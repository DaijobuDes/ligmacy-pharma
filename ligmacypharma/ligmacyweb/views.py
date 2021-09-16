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
        context = {
            'med' : meds
        }
        return render(request, 'dashboard.html', context)