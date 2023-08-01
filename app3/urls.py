from django.urls import path
from app3.views import *
appname='evrything'
urlpatterns=[
    path('index3/',index3,name='index3')
]