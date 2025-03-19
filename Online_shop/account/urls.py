from django.urls import path
from account.views import home

urlpatterns = [
    path("", home , name="home"),

]