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
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .forms import BookForm
from django.views.decorators.csrf import csrf_protect
from django.forms.models import model_to_dict

def home(request):
    #load the landing page
    return render(request, 'home.html')

def queryDB(request,searchString):
    #set some defaults for context
    some_books=[]
    elapsed_time = 0
    num_results = 0
    list_too_long = False
    no_results = True
    empty_search = False
    if request.method == 'GET':
        #title = request.POST.get('search')#get whatever the 
        if len(searchString) == 0: #Disallow empty search, itll just try to return the WHOLE DB and crash and burn in a glorious blaze of light
          return render(request, 'home.html')
        else:
            start = time.perf_counter()# get information on DB Querying performance (potentially optimise it somehow)
            some_books = Books.objects.filter(title__icontains=searchString)
            if len(some_books) == 0:
                return render(request, 'searchResults.html',{'some_books':some_books, 'searchString': searchString, 'elapsed_time':elapsed_time, 'num_results': num_results, 'list_too_long':list_too_long, 'no_results': no_results})
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
                return render(request, 'searchResults.html',{'some_books':some_books, 'title': searchString, 'elapsed_time':elapsed_time, 'num_results': num_results, 'list_too_long':list_too_long, 'no_results': no_results})
    else:
     return HttpResponse(" The request wasnt a POST, this shouldnt happen")


def validate_title(request,title):
   print(f"validating {title}...")
   if request.method == 'GET':
        print(f"title = {title}")
        if not title:
            return JsonResponse({'valid': False, 'error': "No title provided"})
        
        #look through DB for books with the same title
        match_title = Books.objects.filter(title__iexact=title).exists()
        match_orig_title = Books.objects.filter(original_title__iexact=title).exists()

        if not match_title and not match_orig_title:
            print(f"{title} IS valid")
            return JsonResponse({'valid': True})
        else :
            print(f"{title} IS NOT valid")
            return JsonResponse({'valid':False})
   else:
      print(request.method)
      return HttpResponse("Not a GET request")
   
def validate_title_update(request,title,id):
    print(f"validating {title} for update...")
    if request.method == 'GET':
        print(f"title = {title}")
        print(f"book_id = {id}")
        book = book = Books.objects.get(book_id=id)
        check_title = book.title #get old title, the one attached to the book
        print(f"Data to check on : old isbn : {check_title}, new isbn : {title}")
       
        if not title:#ie new title is empty
            return JsonResponse({'valid': False, 'error': "No title provided"})
        
        #check if new title = old title, if yes then its valid
        if title == check_title:
            print("old matches new, we good")
            print(f"{title} IS valid,")
            return JsonResponse({'valid': True})
       
        # if new title not equal old title, ie its been changed, then we need to check if it matches anything else in the DB thats not the old title
        allBooks = Books.objects.all()
        print(f"size of all books : {len(allBooks)}")
        excluding_old_title = allBooks.exclude(title__iexact=check_title).filter(original_title__iexact=check_title)# exclude anything where title matches the old one
        print(f"size of all books excluding the old title : {len(excluding_old_title)}")
        match_title = excluding_old_title.exclude(title__iexact=title).exists()
        match_orig_title = excluding_old_title.filter(original_title__iexact=title).exists()
        if not match_title and not match_orig_title:
            print(f"{title} IS valid")
            return JsonResponse({'valid': True})
        else :
            print(f"{title} IS NOT valid")
            return JsonResponse({'valid':False})
    else:
      print(request.method)
      return HttpResponse("Not a GET request")


def validate_isbn(request,checkIsbn):
   print(f" validating {checkIsbn}...")
   if request.method == 'GET':
        print(f"isbn =  {checkIsbn}")
        if not checkIsbn:
            return JsonResponse({'valid': False, 'error': "No isbn provided"})
        
        #look through DB for books with the same title
        querySet = Books.objects.filter(isbn=checkIsbn)
        match_isbn = querySet.exists()#returns true if the query set isnt empty
        if not match_isbn:
            print(f"{checkIsbn} IS valid")
            return JsonResponse({'valid': True})
        else :
            print(f"{checkIsbn} IS NOT valid")
            return JsonResponse({'valid': False})
   else:
      print(request.method)
      return HttpResponse("Not a GET request")

def validate_isbn_update(request,checkIsbn,id):
    print(f" validating {checkIsbn} for update:")
    if request.method == 'GET':
        print(f"title = {checkIsbn}")
        print(f"book_id = {id}")
        book = book = Books.objects.get(book_id=id)
        check_isbn = book.isbn # get old isbn, the one attached to the book
        print(f"Data to check on : old isbn : {check_isbn}, new isbn : {checkIsbn}")
        if not checkIsbn:#ie if there isnt a new isin to check
            return JsonResponse({'valid': False, 'error': "No title provided"})
       
        #check if new isbn = old isbn, if yes then its valid
        if checkIsbn == check_isbn:
            print("Old and new match we are good")
            print(f"{check_isbn} IS valid")
            return JsonResponse({'valid': True})
        
        # if new isbn not equal old isbn, ie its been changed, then we need to check if it matches anything else in the DB thats not the old isbn
        allBooks = Books.objects.all()
        print(f"size of all books : {len(allBooks)}")
        #exclude all records where isbn = old isbn
        excluding_old_isbn = allBooks.exclude(isbn=check_isbn)
        print(f"size of all books excluding the old isbn : {len(excluding_old_isbn)}")
        #check if there are any recrods that match the new isbn
        match_isbn = excluding_old_isbn.filter(isbn=checkIsbn).exists()

        if not match_isbn:
            print(f"{checkIsbn} IS valid")
            return JsonResponse({'valid': True})
        else :
            print(f"{check_isbn} IS NOT valid")
            return JsonResponse({'valid':False})
    else:
      print(request.method)
      return HttpResponse("Not a GET request")

def validate_isbn13_update(request,checkIsbn13,id):
    print(f" validating {checkIsbn13} for update:")
    if request.method == 'GET':
        print(f"isbn13 = {checkIsbn13}")
        print(f"book_id = {id}")
        book = book = Books.objects.get(book_id=id)
        check_isbn = book.isbn13 # get old isbn, the one attached to the book
        print(f"Data to check on : old isbn : {check_isbn}, new isbn : {checkIsbn13}")
        if not checkIsbn13:#ie if there isnt a new isin to check
            return JsonResponse({'valid': False, 'error': "No title provided"})
       
        #check if new isbn = old isbn, if yes then its valid
        if checkIsbn13 == check_isbn:
            print("Old and new match we are good")
            print(f"{check_isbn} IS valid")
            return JsonResponse({'valid': True})
        
        # if new isbn not equal old isbn, ie its been changed, then we need to check if it matches anything else in the DB thats not the old isbn
        allBooks = Books.objects.all()
        print(f"size of all books : {len(allBooks)}")
        #exclude all records where isbn = old isbn
        excluding_old_isbn = allBooks.exclude(isbn=check_isbn)
        print(f"size of all books excluding the old isbn : {len(excluding_old_isbn)}")
        #check if there are any recrods that match the new isbn
        match_isbn = excluding_old_isbn.filter(isbn=checkIsbn13).exists()

        if not match_isbn:
            print(f"{checkIsbn13} IS valid")
            return JsonResponse({'valid': True})
        else :
            print(f"{check_isbn} IS NOT valid")
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
    

def upload_books(request):
    context = {}
    return render(request, 'deleteBook.html', context )

def delete_book(request, id):
    previous_url = request.META.get('HTTP_REFERER')
    book = get_object_or_404(Books, book_id = id)
    book.delete()
    print("made it past deletion")
    previous_url = request.META.get('HTTP_REFERER')
    if previous_url:
        return redirect(previous_url)
    else:
        return render(request, 'home.html')

def addBook(request):
    return render(request,'addBooks.html', )   

@csrf_protect
def add_book(request):
    print(" made it to the view, the url seems to be working")
    if request.method == 'POST':
        try:
            data = request.POST
            print(f" type of data is {type(data)} adn it looks like : {data}")
            form = BookForm(data)
            if form.is_valid():
                try:
                    print(f"Cleaned data = {form.cleaned_data}")
                    #actually add the book
                    form.save()
                    return JsonResponse({'message':'Book was successfully added'},status=200)
                except Exception as e:
                    print(f"Error during form save {e}")
                    return JsonResponse({'message':'Book was not added','details':str(e)},status=500)
            else:
                return JsonResponse({'message':'Book was not added','errors': form.errors},status=400)
        except Exception as e:
            errors = form.errors
            return JsonResponse({'error':str(e)}, status=500)

def edit_details(request,id):
    if request.method == 'GET':
        book = Books.objects.get(book_id=id)
        book_as_dict  = model_to_dict(book)
        return render(request, 'edit_book.html',{'dictionary':book_as_dict})
    else:
        return HttpResponse("Request was not a get, that shouldnt happen")
    
@csrf_protect
def update_record(request,id):
    print(" made it to the update record view")
    if request.method == 'POST':
        try:
            print(f"about tpo get the dictionary")
            data = request.POST
            print("got the dictionary")
            form = BookForm(data)
            print("about to check form is valid")
            if form.is_valid():
                print("the form is valid")
                print("heres what form looks like ", form.cleaned_data)
                try: 
                    book = Books.objects.get(book_id=id)
                    print(f"got the book {book.title}")
                    book.goodreads_book_id=form.cleaned_data['goodreads_book_id']
                    book.best_book_id=form.cleaned_data['best_book_id'] 
                    book.work_id=form.cleaned_data['work_id'] 
                    book.books_count=form.cleaned_data['books_count']
                    book.isbn=form.cleaned_data['isbn']
                    book.isbn13=form.cleaned_data['isbn13']
                    book.original_publication_year=form.cleaned_data['original_publication_year']
                    book.original_title=form.cleaned_data['original_title']
                    book.title=form.cleaned_data['title']
                    book.language_code=form.cleaned_data['language_code']
                    book.average_rating=form.cleaned_data['average_rating']
                    book.ratings_count=form.cleaned_data['ratings_count']
                    book.work_ratings_count=form.cleaned_data['work_ratings_count']
                    book.work_text_reviews_count=form.cleaned_data['work_text_reviews_count']
                    book.ratings_1=form.cleaned_data['ratings_1']
                    book.ratings_2=form.cleaned_data['ratings_2']
                    book.ratings_3=form.cleaned_data['ratings_3']
                    book.ratings_4=form.cleaned_data['ratings_4']
                    book.ratings_5=form.cleaned_data['ratings_5']
                    book.image_url=form.cleaned_data['image_url']
                    book.small_image_url=form.cleaned_data['small_image_url']
                    for field in book._meta.fields:
                        print(f"{field.name}: {getattr(book, field.name)}")
                    book.save()
                    return JsonResponse({'message':'Record updated successfully'}, status = 200)
                except Exception as e:
                    print(f"Error during form save {e}")
                    return JsonResponse({'message':'Record was not updated','details':str(e)},status=500)
            else:
                print("fomr ")
                return JsonResponse({'message':'Book was not added','errors': form.errors},status=400)
        except Exception as e:
            errors = form.errors
            return JsonResponse({'error':str(e)}, status=500)
    else:
        return HttpResponse("Request was not a post, this shoulnt have happened")

      
    

                
