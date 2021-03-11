from django.conf.urls import include,url
from django.contrib import admin
from . import views
#from .import home


urlpatterns = [

    url('', views.user_list),
]
