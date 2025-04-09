from django.urls import path
from .views import *

urlpatterns = [
    path('contant/', Contant, name='contant'),
    path('thx/', thx, name='thx'),
]