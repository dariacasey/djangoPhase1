from datetime import timezone, datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from .forms import SignUpForm
from .models import Profile


# A lot of this method is from the django documentation.
def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid form submission")
    else:
        form = LoginForm()  # Create an empty form for GET requests

    return render(request, "login.html", {"form": form})


# Also follows structure of method given in django documentation
def signUp_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            is_teacher = form.cleaned_data["is_teacher"]
            is_student = form.cleaned_data["is_student"]

            user = authenticate(username=username, password = password)
            Profile.objects.create(user=user, is_teacher=is_teacher, is_student=is_student)

            login(request, user)
            messages.success(request, "Registration Successful!")
            return redirect("home")
    else:
        form = SignUpForm()

    return render(request, 'registration/sign_up.html', {'form': form})


def logout_user(request):
    if request.user.is_authenticated:
        request.user.profile.last_logout_time = datetime.now()
        request.user.profile.save()
        logout(request)
        messages.success(request, "You Were Logged Out")
    else:
        messages.info(request, "You are already logged out.")
    return redirect('home')
