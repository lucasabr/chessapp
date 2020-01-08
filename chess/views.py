from django.shortcuts import render
from django.http import HttpResponse

messages = [
    {
        'author' : 'Lucasabr',
        'recipient' : 'Jmilicev',
        'message' : 'Whats up',
        'timestamp' : 'Jan 8th, 2019'
    },
    {
        'author' : 'Jmilicev',
        'recipient' : 'Lucasabr',
        'message' : 'Nmu',
        'timestamp' : 'Jan 8th, 2019'
    }
]
def chat(request):
    context = {
        'messages' : messages
    }
    return render(request, 'chess/home.html', context)

def home(request):
    return HttpResponse('<h1>Welcome to Chess<h1>')