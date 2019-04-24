import os
from django.urls import path
from . import views


app_name = os.getcwd().split(os.sep)[-1]
urlpatterns = [
    path('', views.home, name='home'),
]
