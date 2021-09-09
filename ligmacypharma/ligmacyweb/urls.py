from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'ligmacyweb'

urlpatterns = [
    # path('index', views.IndexView.as_view(), name='ligmacyweb_index_view')
    url(r'^$', views.IndexView.as_view(), name='index')
]
