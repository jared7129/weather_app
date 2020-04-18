from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index),  #the path for our index view
]
