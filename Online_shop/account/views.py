from django.shortcuts import render ,redirect
from django.http.response import HttpResponse
from .forms import AccountAuthenticationForm
from django.contrib.auth import authenticate, login, logout





def home(request):
    return render(request, 'account/home2.html', {"name":"amirykta"})
   


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("account:home")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=raw_password)
            if user:
                login(request, user)
                return redirect("account:home")
    else:
        form = AccountAuthenticationForm()

    context["login_form"] = form    

    return render(request, 'account/login.html', context)


