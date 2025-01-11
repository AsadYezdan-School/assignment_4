from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name = "home"),
    path("search-results/<str:searchString>/", views.queryDB,name = "queryDB"),
    path("add-book/", views.addBook, name = "addBook"),
    path("validate-title/<str:title>", views.validate_title, name = "validate-title" ),
    path("validate-isbn/<str:checkIsbn>", views.validate_isbn, name = "validate-isbn" ),
    path("advanced-search/", views.advanced_search, name = "advanced-search"),
    path("upload-books/", views.upload_books, name="upload-books"),
    path("delete-book/id=<int:id>/", views.delete_book,name="delete-book")
]