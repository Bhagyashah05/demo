from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
# password for user bhagya @Shah0000
# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginuser(request):
    if request.method == "POST":
        user=request.POST.get("username")
        pw=request.POST.get("password")
        # print(user,pw)
        # check for correct credentials
        user = authenticate(username=user, password=pw)
        if user is not None:
            login(request,user)
            return redirect("/")
            # A backend authenticated the credentials
        else:
            return render (request,"login.html")

            # No backend authenticated the credentials
    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect("/login")
