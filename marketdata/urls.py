from django.urls import path
from .views import *

urlpatterns = [
    path('startdata/', startdata, name='startdata'),
    path('stopdata/', stopdata, name='stopdata'),
    path('getdata/', getdata, name='getdata'),
]