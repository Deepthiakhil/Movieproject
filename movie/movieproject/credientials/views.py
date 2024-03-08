from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('credientials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('credientials:register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save();
                # messages.info(request, "You're registered successfully")

                return redirect("credientials:login")

        else:
            messages.info(request, "password not matching")
            return redirect('credientials:register')
        return redirect('movieapp:allProCat')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('movieapp:allProCat')
        else:
            messages.info(request, "invalid credientials")
            return redirect('credientials:login')
    return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect('movieapp:allProCat')


def profile(request, id):
    profile = User.objects.get(id=id)
    return render(request, "profile.html", {'profile': profile})


def update(request, id):
    profile = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('movieapp:allProCat')
    return render(request, "edit.html", {'form': form, 'profile': profile})
