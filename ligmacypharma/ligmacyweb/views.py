import time
from django.core.paginator import Page

from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Not the best code but this is to
# shorten the code from below
class PageRedirect():

    def __init__(self, link, msg="Success!"):
        self.link = link
        self.msg = msg

    def redirect(self):
        return "<meta http-equiv='refresh' content='2; url='ligmacyweb/"+self.link+"'><script>function f() { alert('"+self.msg+"'); }</script><body onload='f()'></body>"


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


class ContactView(View):

    def __init__(self):
        pass

    def get(self, request):
        return render(request, "contact.html")


class SignInView(View):

    def __init__(self):
        pass

    def get(self, request):
        return render(request, "sign_in.html")

    def post(self, request):
        data = request.POST
        print(data)

        if data['username'] == '':
            return HttpResponse(PageRedirect("sign_in", msg="No username supplied.").redirect())
            # return HttpResponse("<meta http-equiv='refresh' content='2; url='ligmacyweb/sign_in'><script>function f() { alert('No email supplied.'); }</script><body onload='f()'></body>")
        if data['password'] == '':
            return HttpResponse(PageRedirect("sign_in", msg="No password supplied.").redirect())
            # return HttpResponse("<meta http-equiv='refresh' content='2; url='ligmacyweb/sign_in'><script>function f() { alert('No password supplied.'); }</script><body onload='f()'></body>")

        return render(request, "profile.html")

# Replaced with RegisterView() Class below
# class SignUpView(View):

#     def __init__(self):
#         pass

#     def post(self, request):
#         form = SignUpForm(request.POST)
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         name = request.POST.get("name")
#         age = request.POST.get("age")
#         form = SignUp(email = email, password = password,name = name, age = age)
#         form.save()
#         return HttpResponse("<meta http-equiv='refresh' content='2; url='ligmacyweb/sign_up'><script>function f() { alert('Success!'); }</script><body onload='f()'></body>")
#         return redirect("ligmacyweb:sign_up")

#     def get(self, request):
#         return render(request, "sign_up.html")

class DashboardView(View):

    def __init__(self):
        pass

    def get(self, request):
        meds = Medicine.objects.all()
        accounts = User.objects.all()
        context = {
            'med' : meds,
            'acc' : accounts,
            'user': self.request.user.id
        }
        return render(request, 'dashboard.html', context)

    def post(self, request):
        if 'btnMedicineUpdateSubmit' in request.POST:
            med_id = request.POST.get("med_id")
            med_name = request.POST.get("med_name")
            price = request.POST.get("price")
            stock = request.POST.get("stock")
            Medicine.objects.filter(uid=med_id).update(name=med_name, price=price, stock=stock)
        if 'btnMedicineDeleteSubmit' in request.POST:
            med_id = request.POST.get("med_id")
            Medicine.objects.filter(uid=med_id).delete()

        if 'btnAccountUpdateSubmit' in request.POST:
            user_id = request.POST.get("user_id")
            email = request.POST.get("email")
            name = request.POST.get("name")
            date_joined = request.POST.get("date")
            User.objects.filter(id=user_id).update(email=email, username=name, date_joined= date_joined)
        if 'btnAccountDeleteSubmit' in request.POST:
            user_id = request.POST.get("user_id")
            User.objects.filter(id=user_id).delete()

        # if 'btnAccountUpdateSubmit' in request.POST:
        #     user_id = request.POST.get("user_id")
        #     email = request.POST.get("email")
        #     name = request.POST.get("name")
        #     age = request.POST.get("age")
        #     SignUp.objects.filter(id=user_id).update(email=email, name=name, age=age)
        # if 'btnAccountDeleteSubmit' in request.POST:
        #     user_id = request.POST.get("user_id")
        #     SignUp.objects.filter(id=user_id).delete()

        return HttpResponse(PageRedirect("dashboard").redirect())
        # return HttpResponse("<meta http-equiv='refresh' content='2; url='ligmacyweb/dashboard'><script>function f() { alert('Success!'); }</script><body onload='f()'></body>")


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

        return HttpResponse(PageRedirect("add_medicine").redirect())
        # return HttpResponse("<meta http-equiv='refresh' content='2; url='ligmacyweb/add_medicine'><script>function f() { alert('Success!'); }</script><body onload='f()'></body>")
        # return redirect("ligmacyweb:add_medicine")

    def get(self,request):
        return render(request, "add_medicine.html")


class CartView(View):

    def __init__(self):
        pass

    def get(self, request):
        items = CartItem.objects.all()
        meds = Medicine.objects.all()
        context = {
            'items': items,
            'meds' : meds
        }

        return render(request, "cart.html", context)

    def post(self, request):
        print(request.POST)
        items = CartItem.objects.filter(user_id=User.id)
        meds = Medicine.objects.all()
        context = {
            'items': items,
            'meds' : meds
        }

        if 'btnAddToCart' in request.POST:
            form = None
            med_id = request.POST.get("med_id")
            amount = request.POST.get("amount")
            user_id = request.POST.get("user_id")

            print(type(amount))
            if amount == '0':
                CartItem.objects.filter(user_id=User(user_id=user_id),items_id=Medicine(uid=med_id)).delete()
                return render(request, "cart.html")

            try:
                data = CartItem.objects.get(items_id=Medicine(uid=med_id))
                if data:
                    print("true")
                    CartItem.objects.filter(items_id=Medicine(uid=med_id)).update(amount=amount)
            except:
                print("false")
                form = CartItem(user_id=User(id=user_id), items_id=Medicine(uid=med_id), amount=amount)
                form.save()

            print(form)

        return render(request, "cart.html", context)

# Replacement for SignUpView()
class RegisterView(View):

    def __init__(self):
        pass

    def post(self, request):
        print(request.POST)

        if 'btnRegister' in request.POST:
            form = None
            username = request.POST.get("username")
            password = request.POST.get("password")
            fname = request.POST.get("fname")
            lname = request.POST.get("lname")
            email = request.POST.get("email")

            form = User(
                username=username,
                password=make_password(password=password),
                first_name=fname,
                last_name=lname,
                email=email
            )
            form.save()

        return HttpResponse(PageRedirect("sign_in").redirect())

    def get(self, request):
        return render(request, "register.html")

class ProfileView(View):

    def __init__(self):
        pass

    def get(self, request):
        return render(request, "profile.html")

class StoreView(View):

    def __init__(self):
        pass

    def get(self, request):
        meds = Medicine.objects.all()
        context = {
            'meds': meds
        }

        return render(request, "store.html", context)

    def post(self, request):
        print(request.POST)

        meds = Medicine.objects.all()
        context = {
            'meds': meds
        }

        if 'btnAddToCart' in request.POST:
            form = None
            med_id = request.POST.get("med_id")
            amount = request.POST.get("amount")
            user_id = request.POST.get("user_id")

            print(type(amount))
            if amount == '0':
                CartItem.objects.filter(items_id=Medicine(uid=med_id)).delete()
                return render(request, "cart.html")

            try:
                data = CartItem.objects.get(items_id=Medicine(uid=med_id))
                if data:
                    print("true")
                    CartItem.objects.filter(items_id=Medicine(uid=med_id)).update(amount=amount)
            except:
                print("false")
                form = CartItem(user_id=User(id=user_id), items_id=Medicine(uid=med_id), amount=amount)
                form.save()

            print(form)

        return render(request, "store.html", context)