from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from academic.models import Bulletin


@login_required(login_url="/login")
def index(request):
    return HttpResponse("Hello World {}".format(request.user.username))
    #bulletins = Bulletin.objects.all()
    #return render(request, 'index.html', bulletins)

def adminlogin(request):
    return HttpResponse("Hello World IDAN")

def username(request):
    return HttpResponse("Your username is:"+request.user.username)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse("Unautorized!")
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if (username == ""): return HttpResponse("No username!")
        if (password == ""): return HttpResponse("No password!")
        if (email == ""): return HttpResponse("No email!")
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse("Unautorized!")
        else:
            login(request, user)
            return redirect('/')
    return render(request, "register.html")


def logout_user(request):
    logout(request)
    return HttpResponse("Successfully logged out!")


@login_required(login_url="admin/login")
def dashboard(request):
    if request.method == 'POST':
        body = request.POST['body']
        bulletin = Bulletin()
        bulletin.body = body
        bulletin.save()
    if request.user is None or not request.user.is_staff:
        return HttpResponse("Unauthorized!")
    return render(request, 'admindash.html')