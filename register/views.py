from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    form = UserCreationForm()
    return render(request, 'register/register.html', {'form' : form})
