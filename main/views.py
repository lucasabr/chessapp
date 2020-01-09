from django.shortcuts import render


def home(request):
    return render(request, 'main/base.html',{"current":"home"}) 