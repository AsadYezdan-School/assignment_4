from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import time
from .models import Books
from .models import BookTags
from .models import Ratings
from .models import Tags
from .models import ToRead
import json

def home(request):
    #load the landing page
    return render(request, 'home.html')

def queryDB(request):
    #set some defaults for context
    some_books=[]
    elapsed_time = 0
    num_results = 0
    list_too_long = False
    no_results = True
    empty_search = False
    if request.method == 'POST':
        title = request.POST.get('search')#get whatever the 
        if len(title) == 0: #Disallow empty search, itll just try to return the WHOLE DB and crash and burn in a glorious blaze of light
          return render(request, 'home.html')
        else:
            start = time.perf_counter()# get information on DB Querying performance (potentially optimise it somehow)
            some_books = Books.objects.filter(title__icontains=title)
            if len(some_books) == 0:
                return render(request, 'searchResults.html',{'some_books':some_books, 'title': title, 'elapsed_time':elapsed_time, 'num_results': num_results, 'list_too_long':list_too_long, 'no_results': no_results})
            else:
                #if we get here (the hope is to get here almost always)we're all good to post results
                #SQL Raw Query : SELECT book_id,authors, title FROM books WHERE title LIKE '%{title}%';
                end = time.perf_counter()
                elapsed_time = end - start
                elapsed_time = round(elapsed_time,3)
                num_results = len(some_books)
                list_too_long = False
                no_results = False
                if len(some_books)>100:
                    some_books = some_books[:100]
                    list_too_long = True
                return render(request, 'searchResults.html',{'some_books':some_books, 'title': title, 'elapsed_time':elapsed_time, 'num_results': num_results, 'list_too_long':list_too_long, 'no_results': no_results})
    else:
     return HttpResponse(" The request wasnt a POST, this shouldnt happen")

def addBook(request):
    return render(request,'addBooks.html', )


def validate_title(request):
   print(" made it to the validation method!")
   if request.method == 'GET':
        title = request.GET.get('validate', '')
        print(f"title = {title}")
        if not title:
            return JsonResponse({'valid': False, 'error': "No title provided"})
        
        #look through DB for books with the same title
        match_title = Books.objects.filter(title__iexact=title).exists()
        match_orig_title = Books.objects.filter(original_title__iexact=title).exists()
        print("made it past the querying")
        if not match_title and not match_orig_title:
            return JsonResponse({'valid': True})
        else :
            return JsonResponse({'valid':False})
   else:
      print(request.method)
      return HttpResponse("Not a GET request")
      
  
   


      
    

                
