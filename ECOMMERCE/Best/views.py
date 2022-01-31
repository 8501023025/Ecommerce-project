from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.
def home(request):
    return render(request,'base.html')

def first(request):
    return render(request,'about.html')

def second(request):
    return render(request,'contact.html')


def third(request):
    return render(request,'index.html')

def fourth(request):
    obj = products.objects.all()
    return render(request,'products.html',{'data':obj})

def product_detailss(request,slug):
    pro = products.objects.get(slug = slug)
    return render(request,'product_details.html',{'info':pro})

def p_search(request):
    if request.method == 'POST':          
        N=request.POST['SEARCH']   
        obj = products.objects.filter(name__contains=N)
        return render (request,'search.html',{'mint':obj})
    else:
        return render (request,'search.html')
    
    return render(request,'search.html')

def reg(request):
    if request.method == 'POST':
        form = Registration_user(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log')
        else:
            messages.error(request,'something went wrong')
            return render(request,'register.html',{'form':form})
            
    else:
        form = Registration_user()
        return render(request,'register.html',{'form':form})
    
    
def log(request):
    if request.method =='POST':
        U=request.POST['username']
        P=request.POST['pass']
        obj = authenticate(request,username =U,password =P)
        if obj is not None:
            login(request,obj)
            return redirect('home')
        else:
            messages.error(request,'Invalid crediantials')
            return render (request,'login.html')
    else :
         return render (request,'login.html')
        
           
    
    
    



