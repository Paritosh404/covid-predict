

from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:    
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

def adm(request):
    return HttpResponseRedirect("http://127.0.0.1:8000/admin/login/")

def register(request):
    if request.user.is_authenticated:
        return render(request,'login.html')
    else:
        
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
    




def logout(request):
    auth.logout(request)
    return redirect('register')

def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return render(request,'login.html')

def update(request):
    if request.user.is_authenticated:

        if request.method=='POST':
            name=request.user.username
            print(name)
            q1 = request.POST['q1']
            q2 = request.POST['q2']
            q3 = request.POST['q3']
            q4 = request.POST['q4']
            q5 = request.POST['q5']
            q6 = request.POST['q6']

            updt2 = Data.objects.filter(Name=name)
            if Data.objects.filter(Name=name).exists():
            
                updt2.Q1=q1
                updt2.Q2=q2
                updt2.Q3=q3
                updt2.Q4=q4
                updt2.Q5=q5
                updt2.Q6=q6
                updt2.update()
                return render(request,'index.html')

            else:
                updt = Data.objects.create(Name=name,Q1=q1 , Q2=q2 , Q3=q3 , Q4=q4 , Q5=q5 , Q6=q6)
                updt.save()
                return render(request,'index.html')
        else:
            return render(request,'update.html')
    else:
        return render(request,'login.html')

def result(request):
    if request.user.is_authenticated:
        name=request.user.username
        if Data.objects.filter(Name=name).exists():

            ques = Data.objects.get(Name=request.user.username)
            
            if ques.Q1=='true' and ques.Q2=='true' and ques.Q3=='true' and ques.Q4=='true' and ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'VERY CRITICAL PLEASE CONTACT HEALTH DEPARTMENT GET TESTED FOR COVID IMMEDIATELY AND TRY TO MAINTAIN DISTANCE TO ALL '})
            elif ques.Q1=='true' and ques.Q2=='true' and ques.Q3=='true' and ques.Q4=='true' and ques.Q5=='true':
                return render(request,'result.html',{'msg':'VERY CRITICAL PLEASE CONTACT HEALTH DEPARTMENT GET TESTED FOR COVID IMMEDIATELY AND TRY TO MAINTAIN DISTANCE TO ALL '})
            elif ques.Q1=='true' and ques.Q2=='true' and ques.Q3=='true' and ques.Q4=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'VERY CRITICAL PLEASE CONTACT HEALTH DEPARTMENT GET TESTED FOR COVID IMMEDIATELY AND TRY TO MAINTAIN DISTANCE TO ALL '})  
            elif ques.Q1=='true' and ques.Q2=='true' and ques.Q3=='true' and ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'VERY CRITICAL PLEASE CONTACT HEALTH DEPARTMENT GET TESTED FOR COVID IMMEDIATELY AND TRY TO MAINTAIN DISTANCE TO ALL '})
            elif ques.Q1=='true' and ques.Q2=='true' and ques.Q4=='true' and ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'VERY CRITICAL PLEASE CONTACT HEALTH DEPARTMENT GET TESTED FOR COVID IMMEDIATELY AND TRY TO MAINTAIN DISTANCE TO ALL '})
            elif ques.Q1=='true' and ques.Q3=='true' and ques.Q4=='true' and ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'VERY CRITICAL PLEASE CONTACT HEALTH DEPARTMENT GET TESTED FOR COVID IMMEDIATELY AND TRY TO MAINTAIN DISTANCE TO ALL '})
            elif ques.Q2=='true' and ques.Q3=='true' and ques.Q4=='true' and ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q2=='true' and ques.Q3=='true' and ques.Q4=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q2=='true' and ques.Q3=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q2=='true' and ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q4=='true' and ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif  ques.Q3=='true' and ques.Q4=='true' and ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q2=='true' and ques.Q3=='true' and ques.Q5=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q2=='true' and ques.Q4=='true' and ques.Q5=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q3=='true' and ques.Q4=='true' and ques.Q5=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q2=='true' and ques.Q3=='true' and ques.Q4=='true' and ques.Q5=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q2=='true' and ques.Q4=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q3=='true' and ques.Q4=='true'  and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q2=='true' and ques.Q3=='true' and ques.Q4=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q1=='true'and ques.Q3=='true'  and ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q2=='true' and ques.Q3=='true'  and ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q2=='true' and ques.Q4=='true' and ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q2=='true' and ques.Q3=='true' :
                return render(request,'result.html',{'msg':'MODERATE RISK STAY AT HOME STAY SAFE'})
            elif ques.Q1=='true' and ques.Q2=='true'and ques.Q4=='true':
                return render(request,'result.html',{'msg':'MODERATE RISK STAY AT HOME STAY SAFE'})
            elif ques.Q1=='true' and ques.Q2=='true' and ques.Q5=='true':
                return render(request,'result.html',{'msg':'MODERATE RISK STAY AT HOME STAY SAFE'})
            elif ques.Q1=='true' and ques.Q2=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q3=='true'  and ques.Q4=='true' :
                return render(request,'result.html',{'msg':'MODERATE RISK STAY AT HOME STAY SAFE'})
            elif ques.Q1=='true' and ques.Q3=='true' and ques.Q5=='true' :
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q3=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q4=='true' and  ques.Q5=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING STAY EXTRA CAUTIOUS'})
            elif ques.Q1=='true' and ques.Q4=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'VERY CRITICAL PLEASE CONTACT HEALTH DEPARTMENT GET TESTED FOR COVID IMMEDIATELY AND TRY TO MAINTAIN DISTANCE TO ALL'})
            elif ques.Q1=='true' and ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'VERY CRITICAL PLEASE CONTACT HEALTH DEPARTMENT GET TESTED FOR COVID IMMEDIATELY AND TRY TO MAINTAIN DISTANCE TO ALL'})
            elif ques.Q2=='true' and ques.Q3=='true' and ques.Q4=='true' :
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q2=='true' and ques.Q3=='true'and ques.Q5=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q2=='true' and ques.Q3=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING STAY EXTRA CAUTIOUS'})
            elif ques.Q2=='true' and ques.Q4=='true' and ques.Q5=='true':
                return render(request,'result.html',{'msg':'VERY CRITICAL PLEASE CONTACT HEALTH DEPARTMENT GET TESTED FOR COVID IMMEDIATELY AND TRY TO MAINTAIN DISTANCE TO ALL'})
            elif ques.Q2=='true' and ques.Q4=='true'  and ques.Q6=='true' :
                return render(request,'result.html',{'msg':'VERY CRITICAL PLEASE CONTACT HEALTH DEPARTMENT GET TESTED FOR COVID IMMEDIATELY AND TRY TO MAINTAIN DISTANCE TO ALL'})
            elif ques.Q2=='true' and ques.Q5=='true' and ques.Q6=='true' :
                return render(request,'result.html',{'msg':'VERY CRITICAL PLEASE CONTACT HEALTH DEPARTMENT GET TESTED FOR COVID IMMEDIATELY AND TRY TO MAINTAIN DISTANCE TO ALL'})
            elif ques.Q3=='true' and ques.Q4=='true' and ques.Q5=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING STAY EXTRA CAUTIOUS'})
            elif ques.Q3=='true' and ques.Q4=='true' and  ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING STAY EXTRA CAUTIOUS'})
            elif ques.Q3=='true' and ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'VERY CRITICAL PLEASE CONTACT HEALTH DEPARTMENT GET TESTED FOR COVID IMMEDIATELY AND TRY TO MAINTAIN DISTANCE TO ALL'})
            elif ques.Q4=='true' and ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'VERY CRITICAL PLEASE CONTACT HEALTH DEPARTMENT GET TESTED FOR COVID IMMEDIATELY AND TRY TO MAINTAIN DISTANCE TO ALL'})
            elif ques.Q1=='true' and ques.Q2=='true':
                return render(request,'result.html',{'msg':'INFECTION RATE MODERATE MAINTAIN SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q3=='true':
                return render(request,'result.html',{'msg':'INFECTION RATE MODERATE MAINTAIN SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q4=='true':
                return render(request,'result.html',{'msg':'INFECTION RATE MODERATE MAINTAIN SOCIAL DISTANCING'})
            elif ques.Q1=='true' and ques.Q5=='true':
                return render(request,'result.html',{'msg':'INFECTION RATE MODERATE MAINTAIN SOCIAL DISTANCING TEST AGAIN IF SYMTOMS APPEAR'})
            elif ques.Q1=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'INFECTION RATE MODERATE MAINTAIN SOCIAL DISTANCING TEST AGAIN IF SYMTOMS APPEAR'})
            elif ques.Q2=='true' and ques.Q3=='true':
                return render(request,'result.html',{'msg':'INFECTION RATE MODERATE MAINTAIN SOCIAL DISTANCING'})
            elif ques.Q2=='true' and ques.Q4=='true':
                return render(request,'result.html',{'msg':'INFECTION RATE MODERATE MAINTAIN SOCIAL DISTANCING TEST AGAIN IF SYMTOMS GROWS'})
            elif ques.Q2=='true' and ques.Q5=='true':
                return render(request,'result.html',{'msg':'INFECTION RATE MODERATE MAINTAIN SOCIAL DISTANCING TEST AGAIN IF SYMTOMS APPEAR'})
            elif ques.Q2=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'INFECTION RATE MODERATE MAINTAIN SOCIAL DISTANCING TEST AGAIN IF SYMTOMS APPEAR'})
            elif ques.Q3=='true' and ques.Q4=='true':
                return render(request,'result.html',{'msg':'INFECTION RATE MODERATE MAINTAIN SOCIAL DISTANCING TEST AGAIN IF SYMTOMS GROWS'})
            elif ques.Q3=='true' and ques.Q5=='true':
                return render(request,'result.html',{'msg':'INFECTION RATE MODERATE MAINTAIN SOCIAL DISTANCING TEST AGAIN IF SYMTOMS APPEAR'})
            elif ques.Q3=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'INFECTION RATE MODERATE MAINTAIN SOCIAL DISTANCING TEST AGAIN IF SYMTOMS APPEART'})
            elif ques.Q4=='true' and ques.Q5=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q4=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING'})
            elif ques.Q5=='true' and ques.Q6=='true':
                return render(request,'result.html',{'msg':'COULD BE CRITICAL PLEASE CONTACT HEALTH DEPARTMENT AND ENSURE SOCIAL DISTANCING STAY EXTRA CAUTIOUS'})
            elif ques.Q1=='true':
                return render(request,'result.html',{'msg':'LOW RISK STAY AT HOME AND MAINTAIN SOCIAL DISTANCING'})
            elif ques.Q2=='true':
                return render(request,'result.html',{'msg':'LOW RISK YOU ARE SAFE MAINTAIN SOCIAL DISTANCING'})
            elif ques.Q3=='true':
                return render(request,'result.html',{'msg':'LOW RISK STAY AT HOME AND MAINTAIN SOCIAL DISTANCING'})
            elif ques.Q4=='true':
                return render(request,'result.html',{'msg':'LOW RISK STAY AT HOME AND MAINTAIN SOCIAL DISTANCING'})
            elif ques.Q5=='true':
                return render(request,'result.html',{'msg':'LOW RISK YOU ARE SAFE MAINTAIN SOCIAL DISTANCING'})
            elif ques.Q6=='true':
                return render(request,'result.html',{'msg':'INFECTION RATE MODERATE MAINTAIN SOCIAL DISTANCING TEST AGAIN IF SYMTOMS APPEAR'})
            else:
                return render(request,'result.html',{'msg':'LOW RISK YOU ARE SAFE'})
    
        else:
            return render(request,'update.html')
    else:
        return render(request,'login.html')

        
    

def info(request):
    if request.user.is_authenticated:
        return render(request,'info.html')
    else:
        return render(request,'login.html')
    
    