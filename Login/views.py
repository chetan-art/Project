
# Create your views here.
from django.shortcuts import render,redirect
from Login.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from Login.decoraters import unauthenticated_user,allowed_user
from Home.views import Home
# Create your views here.
# This section is for signup for the new user

@unauthenticated_user
def Signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Signup successfull')
            return redirect('http://127.0.0.1:8000/Loginup/')
    context = {'form':form}
    return render(request,'Signup.html',context)
# This section is for login for the existing user
# Here we use the decorater which we create in decoraters.py
#this function is user login the user
@unauthenticated_user
def Loginup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('http://127.0.0.1:8000/Home/')
        else:
            messages.info(request,"Username or Password is incorrect")
    List1={}
    return render(request,'Login.html',List1)



# This is section for logout for the user
def LogoutPage(request):
    logout(request)
    # this is the redirect page where the user goes after the Logout
    return redirect('http://127.0.0.1:8000/Home/')