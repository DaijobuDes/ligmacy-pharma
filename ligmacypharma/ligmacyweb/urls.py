from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'ligmacyweb'

urlpatterns = [
    # path('index', views.IndexView.as_view(), name='ligmacyweb_index_view')
    # url(r'^$', views.IndexView.as_view(), name='index'),
    path(r'/', views.IndexView.as_view(), name='index'),
    # url(r'/', views.IndexView.as_view(), name='index'),
    url(r'about', views.AboutView.as_view(), name='about'),
    url(r'contact', views.ContactView.as_view(), name='contact'),
    url(r'sign_in', views.SignInView.as_view(), name='sign_in'),
    url(r'sign_up', views.SignUpView.as_view(), name='sign_up'),
    url(r'dashboard', views.DashboardView.as_view(), name='dashboard'),
    url(r'add_medicine', views.Add_MedicineView.as_view(), name='add_medicine'),
    url(r'cart', views.CartView.as_view(), name='cart'),
    url(r'register', views.RegisterView.as_view(), name='register'),
]
