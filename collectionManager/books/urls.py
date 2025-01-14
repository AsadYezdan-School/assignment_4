from django.urls import path, include
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
    path("validate-isbn13-update/<str:checkIsbn13>/<int:id>/", views.validate_isbn13_update, name = "validate-isbn13-update" ),
    path("advanced-search/", views.advanced_search, name = "advanced-search"),
    path("upload-books/", views.upload_books, name="upload-books"),
    path("delete-book/id=<int:id>/", views.delete_book,name="delete-book"),
    path("edit-details/id=<int:id>/",views.edit_details,name="edit-details"),
    path("update-record/<int:id>", views.update_record, name = 'updateRecord'),
    path("bulkAdd/", views.bulk_add_books, name = 'bulk-add-books'),
    path("bulkAdd/validateJSON/", views.validateJSON,name='validateJSON'),
    path("bulkAdd/addFromJSON/", views.addFromJSON,name='addFromJSON'),
    path("add-rating/<int:id>",views.add_rating, name = "add-rating"),
    path("submit-rating/", views.submit_rating, name = "submit-rating"),
    path("add-to-read/<int:id>",views.add_to_read, name = "add-to-read"),
    path("submit-to-read/", views.submit_to_read, name = "submit-to-read"),
    path("lookAtList/",views.lookAtList, name = "LookAtList"),
    path("view-to-read/<int:id>/", views.view_to_read, name = "view-to-read"),
]