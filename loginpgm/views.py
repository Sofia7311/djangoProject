
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout


# Create your views here.
from verify_email.email_handler import send_verification_email


def loginPage(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Index')
        else:
            error = "Username or password is incorrect. Please try again!!"
            return render(request, 'login.html', {'form': form, 'error': error})
    else:
        form = UserCreationForm()
        return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        verify_msg = ''
        if form.is_valid():
            send_verification_email(request, form)
            verify_msg = "A verification link has been sent to your email address. Please check and validate your email"
        return render(request, 'register.html', {'form': form, 'verify_msg': verify_msg})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('loginPage')

           return redirect('loginPage')
        else:
           return render(request, 'register.html', {'form':form})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('loginPage')
