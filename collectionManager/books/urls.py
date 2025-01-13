from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name = "home"),
    path("search-results/<str:searchString>/", views.queryDB,name = "queryDB"),
    path("add-book/", views.addBook, name = "addBook"),
    path("add-book/add-record/", views.add_book,name="add_book"),
    path("validate-title/<str:title>", views.validate_title, name = "validate-title" ),
    path("validate-title-update/<str:title>/<int:id>/", views.validate_title_update, name = "validate-title-update" ),
    path("validate-isbn/<str:checkIsbn>", views.validate_isbn, name = "validate-isbn" ),
    path("validate-isbn-update/<str:checkIsbn>/<int:id>/", views.validate_isbn_update, name = "validate-isbn-update" ),
    path("validate-isbn13-update/<str:checkIsbn13>/<int:id>/", views.validate_isbn13_update, name = "validate-isbn-update" ),
    path("advanced-search/", views.advanced_search, name = "advanced-search"),
    path("upload-books/", views.upload_books, name="upload-books"),
    path("delete-book/id=<int:id>/", views.delete_book,name="delete-book"),
    path("edit-details/id=<int:id>/",views.edit_details,name="edit-details"),
    path("update-record/<int:id>", views.update_record, name = 'updateRecord'),
]