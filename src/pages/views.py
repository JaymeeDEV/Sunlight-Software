from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>") # Returns HTML in browser
