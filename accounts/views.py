from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from . models import login_detailes

# Create your views here.

# def register(request):
#     return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

@login_required(login_url='login')
def index(request):
    #obj=Rides.objects.all()
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
             
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:   
             if User.objects.filter(username=username).exists():
                 messages.info(request,"Username Already Exists")
                 return redirect('register') 
             elif User.objects.filter(password=password).exists():
                 messages.info(request,"Password Already Exists")
                 return redirect('register') 
             else:
                user=User.objects.create_user(username=username,password=password)
                login_detailes(username=username,password=password).save
                user.save();
        print("User Created");
        return redirect('login')
        #zzz else:
        #     messages.info(request,"password not match")
        #     return redirect('register')
    return render(request, 'register.html')
    

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('name')
        else:
            messages.info(request,"invalid values")
            return redirect('login')     
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('login')