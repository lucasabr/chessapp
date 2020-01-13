from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def home(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form' : form})

def profile(request):
    return render(request, 'register/profile.html')
