from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("search-results/", views.queryDB,name = "queryDB"),
    path("add-book/", views.addBook, name = "addBook"),
    path("validate-title/", views.validate_title, name = "validate-title" ),
    path("advanced-search/", views.advanced_search, name = "advanced-search"),
]