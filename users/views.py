from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import userRegisterForm
from .signals import userProfileCreation


def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            pass

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'users/userLogin.html')


def userLogout(request): 
    logout(request)
    return redirect('login')

def userRegister(request):
    form = userRegisterForm()

    if request.method == "POST":
        form =  userRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'users/userRegister.html', context)