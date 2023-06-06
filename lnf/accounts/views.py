
from datetime import date
from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout


from datetime import datetime


# signup
def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, "Account Created Successfully!!")
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, "accounts/signup.html", {"form": fm})


# Login View
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data["username"]
                upass = fm.cleaned_data["password"]
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfully")
                    return HttpResponseRedirect("/index/")
        else:
            fm = AuthenticationForm()
        return render(request, "accounts/userlogin.html", {"form": fm})
    else:
        return HttpResponseRedirect("/index/")


# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/index/")

    

def index(request):
    if request.user.is_authenticated:
        return render(request, "accounts/index.html")
    else:
        return HttpResponseRedirect("/")


def lost_items(request):
    if request.user.is_authenticated:
        return render(request, "accounts/lost.html")
    else:
        return HttpResponseRedirect("/")

def found_items(request):
    if request.user.is_authenticated:
        return render(request, "accounts/found.html")
    else:
        return HttpResponseRedirect("/")

def report_lost_items(request):
    if request.user.is_authenticated:
        return render(request, "accounts/index.html")
    else:
        return HttpResponseRedirect("/")

def report_found_items(request):
    if request.user.is_authenticated:
        return render(request, "accounts/index.html")
    else:
        return HttpResponseRedirect("/")
def claim(request):
    if request.user.is_authenticated:
        return render(request, "accounts/index.html")
    else:
        return HttpResponseRedirect("/")


def faq(request):
    if request.user.is_authenticated:
        return render(request, "accounts/index.html")
    else:
        return HttpResponseRedirect("/")
    
def contact(request):
    if request.user.is_authenticated:
        return render(request, "accounts/index.html")
    else:
        return HttpResponseRedirect("/")