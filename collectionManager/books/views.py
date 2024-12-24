from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to home page broski.")

def queryDB(request):
    return HttpResponse("Here is where i shall put query results")


