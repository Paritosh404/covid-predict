

from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.



def adm(request):
    return HttpResponseRedirect("http://127.0.0.1:8000/admin/login/")

def register(request):

    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                print('Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                print('Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1, email=email , first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request,'User created')
                print('User created')
                return redirect('login')
        else:
            messages.info(request,'Password not maching')
            print('password not maching')
            return redirect('register')
        return render(request, 'register.html')
    else:
        return render(request,'register.html')


def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('register')

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request,'login.html')

def update(request):
    if request.method=='POST':
        name=request.user.username
        print(name)
        q1 = request.POST['q1']
        q2 = request.POST['q2']
        q3 = request.POST['q3']
        q4 = request.POST['q4']
        q5 = request.POST['q5']
        q6 = request.POST['q6']

        updt2 = Data.objects.get(Name=name)
        if updt2.Name==name:
            
            updt2.Q1=q1
            updt2.Q2=q2
            updt2.Q3=q3
            updt2.Q4=q4
            updt2.Q5=q5
            updt2.Q6=q6
            updt2.save()
            return render(request,'index.html')

        else:
            updt = Data.objects.create(Name=name,Q1=q1 , Q2=q2 , Q3=q3 , Q4=q4 , Q5=q5 , Q6=q6)
            updt.save()
            return render(request,'index.html')
    else:
        return render(request,'update.html')

def result(request):
    pass