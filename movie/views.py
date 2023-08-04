from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse('<h1>Welome to Home Page</h1>')
    # return render(request, 'home.html')
    return render(request, 'home.html', {'name':'Julio César'})

def about(request):
    return render(request, 'about.html')