from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    '''
    Requiremnets for home page:
        Register a enw user
    '''
    return HttpResponse("Welcome to home page broski.")

def queryDB(request):
    return HttpResponse("Here is where i shall put query results")
    

# Create your views here.

