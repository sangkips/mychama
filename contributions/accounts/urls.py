from django.conf.urls import url
from django.urls import path, include
from . import  views

urlpatterns = [

 #   path('register/', views.register, name='register')
    url(r'^', views.index, name='index'),
]


