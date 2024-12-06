from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to da home page broski.")


# Create your views here.

