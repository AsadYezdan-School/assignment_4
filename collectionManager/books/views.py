from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import time
from django.db.models import Q
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

def advanced_search(request):
    start = time.perf_counter()
    #get the fields and make a dictionary
    fields ={
    'title':request.POST.get('full_title') or "",
    'authors':request.POST.get('authors') or "",
    'isbn':request.POST.get('isbn') or "",
    'year_published':request.POST.get('publication_year') or "",
    'lang_code':request.POST.get('lang_code') or "",
    'avg_rating':request.POST.get('avgRating') or "",
    'rating_count':request.POST.get('ratingsCount') or "",
    }
    print(f'the fields dictionary :{fields}')
    if any(value !='' for value in fields.values()):
     #if any of the fields are full
     do_search = True
     some_books=Books.objects.all()
     print(f"getting the whole set: {len(some_books)}")
    
    else:
        #return a standard landing page
        some_books =[]
        elapsed_time = 0
        num_results = 0
        no_results=False
        do_search = False
        return render(request,'advancedSearch.html',{'some_books':some_books, 'elapsed_time': elapsed_time, 'num_results': num_results, 'fields': fields, 'no_results' : no_results, 'do_search': do_search})

    for key, value in fields.items():
        if value != '':# if field wasnt left empty
            if key == 'title':
                print('non empty title : ', value)
                some_books = some_books.filter(Q(title__icontains=value) | Q(original_title__icontains=value))
                print(f"lenght of some_books after filter = {len(some_books)}")
            elif key == 'authors':
                print("non empty authors: ", value)
                some_books = some_books.filter(authors__icontains=value)
                print(f"lenght of some_books after filter = {len(some_books)}")
            elif key == 'isbn':
                print("non empty isbn found : ", value)
                some_books= some_books.filter(isbn__icontains=value)
                print(f"lenght of some_books after filter = {len(some_books)}")
            elif key == 'year_published':
                print(" non empty year found : ", value)
                if "<" in value or ">" in value: #check if a > or < than is used if not
                    parameters = value.split()
                    print(parameters)
                    if parameters[0].strip() == '>':
                        print(" year greater than", parameters[1])
                        some_books=some_books.filter(original_publication_year__gt=parameters[1].strip())
                        print(f"lenght of some_books after filter = {len(some_books)}")
                    elif parameters[0].strip() == '<':
                        print(" year less than", parameters[1])
                        some_books.filter(original_publication_year__lt=parameters[1].strip())
                        print(f"lenght of some_books after filter = {len(some_books)}")
                    else:
                        some_books = some_books.filter(original_publication_year=parameters[1].strip())
                        print(f"lenght of some_books after filter = {len(some_books)}")
                else:
                    #default mode is exact comparison
                    some_books = some_books.filter(original_publication_year=value)
                    print(f"lenght of some_books after filter = {len(some_books)}")
            elif key == 'lang_code':
                print("non empty lang_code found", value )
                some_books = some_books.filter(language_code=value)
                print(f"lenght of some_books after filter = {len(some_books)}")
            elif key == 'avg_rating':
                print(" non empty avg rating : ", value)
                if "<" in value or ">" in value: #check if a > or < than is used if not
                    parameters = value.split()
                    print(parameters)
                    if parameters[0].strip() == '>':
                        print(" avg rating greater than", parameters[1])
                        print(f"length of some_books before filter = {len(some_books)}")
                        some_books=some_books.filter(average_rating__gt=parameters[1].strip())
                        print(f"lenght of some_books after filter = {len(some_books)}")
                    elif parameters[0].strip() == '<':
                        print(" avg rating less than", parameters[1])
                        print(f"length of some_books before filter = {len(some_books)}")
                        some_books.filter(average_rating__lt=parameters[1].strip())
                        print(f"lenght of some_books after filter = {len(some_books)}")
                    else:
                        print(" no operators found")
                        some_books = some_books.filter(average_rating=parameters[1].strip())
                        print(f"lenght of some_books after filter = {len(some_books)}")
                else:
                    #default mode is exact comparison
                    some_books = some_books.filter(average_rating=value)
                    print(f"lenght of some_books after filter = {len(some_books)}")
            elif key == 'rating_count':
                print(" non empty rating count : ", value)
                if "<" in value or ">" in value: #check if a > or < than is used if not
                    parameters = value.split()
                    print(parameters)
                    if parameters[0].strip() == '>':
                        print(" rating count greater than", parameters[1])
                        some_books=some_books.filter(ratings_count__gt=parameters[1].strip())
                    elif parameters[0].strip() == '<':
                        print(" rating count less than", parameters[1])
                        some_books.filter(ratings_count__lt=parameters[1].strip())
                    else:
                        print(" no operators found")
                        some_books = some_books.filter(ratings_count=parameters[1].strip())
                else:
                    #default mode is exact comparison
                    some_books = some_books.filter(ratings_count=value)
    end = time.perf_counter()
    no_results = False
    elapsed_time = end - start
    elapsed_time = round(elapsed_time,2)
    num_results = len(some_books)
    if len(some_books)==0:
        no_results=True
    return render(request,'advancedSearch.html',{'some_books':some_books, 'elapsed_time': elapsed_time, 'num_results': num_results, 'fields': fields, 'no_results' : no_results, 'do_search': do_search})
    

   


      
    

                
