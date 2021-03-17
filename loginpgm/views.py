
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

# Create your views here.


def loginPage(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password1']
        user  = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Index')
        else:
            #messages.info(request, "Username or password is incorrect. Please try again!!")
            error = "Username or password is incorrect. Please try again!!"
            return render(request, 'login.html', {'form':form, 'error':error})
    else:
        form = UserCreationForm()
        return render(request, 'login.html', {'form':form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
           form.save()

           return redirect('loginPage')
        else:
           return render(request, 'register.html', {'form':form})
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('loginPage')
