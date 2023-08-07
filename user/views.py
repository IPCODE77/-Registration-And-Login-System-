from django.shortcuts import render,redirect
from user.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout



# Create your views here.

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.error(request , 'Username Already Exits')
            return redirect('/register/')
            

        user = User.objects.create(
            first_name = firstname,
            last_name = lastname,
            username = username,
            email = email
        )
        user.set_password(password)
        user.save()
        # messages.error(request, "Account Created Successfully")
        return redirect('/login/')
    context = {'link':'Account Create'}

    return render(request , 'html/register.html' , context)

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username ).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        user = authenticate(username = username , password = password)
        if user is None:
                messages.error(request , 'invalid password')
                return redirect('/login/')
        else:
             login(request,user)
             return redirect('/success/')
    context = {'link':'Log in'}

    return render(request, 'html/login.html',context)

def success(request):
    context = {'link':'Success'}

    return render(request, 'html/success.html',context)

def user_logout(request):
    logout(request)
    return redirect('/login/')