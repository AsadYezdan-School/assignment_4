from django import forms
from .models import Books
from .models import Ratings
from .models import ToRead

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ["goodreads_book_id",
                  "best_book_id",
                  "work_id",
                  "books_count",
                  "isbn",
                  "isbn13",
                  "authors",
                  "original_publication_year",
                  "original_title",
                  "title",
                  "language_code",
                  "average_rating",
                  "ratings_count",
                  "work_ratings_count",
                  "work_text_reviews_count",
                  "ratings_1",
                  "ratings_2",
                  "ratings_3",
                  "ratings_4",
                  "ratings_5",
                  "image_url",
                  "small_image_url"]

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = ['user_id', 'book_id', 'rating']

    # Custom validation to ensure rating is between 0 and 5
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating is not None and (rating < 0 or rating > 5):
            raise forms.ValidationError("Rating must be between 0 and 5.")
        return rating

class ToReadForm(forms.ModelForm):
    class Meta:
        model = ToRead
        fields = ['user_id', 'book_id']

    def clean_user_id(self):
        user_id = self.cleaned_data.get('user_id')
        if user_id is None or user_id <= 0 or user_id > 53432:
            raise forms.ValidationError("Invalid user ID.")
        return user_id

    def clean_book_id(self):
        book_id = self.cleaned_data.get('book_id')
        if book_id is None or book_id <= 0:
            raise forms.ValidationError("Invalid book ID.")
        return book_id


