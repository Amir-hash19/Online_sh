from django.shortcuts import render
from django.http.response import HttpResponse

def home(request):
    return render(request, 'account/home2.html', {"name":"amirykta"})
   
