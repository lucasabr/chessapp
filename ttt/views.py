from django.shortcuts import render

def home(request):
    return render(request, 'ttt/home.html', {'current':'ttt'})
