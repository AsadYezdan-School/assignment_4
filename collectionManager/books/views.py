from django.shortcuts import render
from django.http import HttpResponse
from .models import Books
from .models import BookTags
from .models import Ratings
from .models import Tags
from .models import ToRead

def home(request):
    return render(request, 'home.html')

def queryDB(request):
    some_books = Books.objects.raw('SELECT book_id,authors, title FROM books LIMIT 5;')
    return render(request, 'books.html',{'some_books':some_books})

                
