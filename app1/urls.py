from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('index1/',index1,name='index1')
]