from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def david(request):
    return HttpResponse("david","Hello, David")

def test(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })