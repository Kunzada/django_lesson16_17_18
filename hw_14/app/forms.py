from django import forms 
from .models import Book,Author,Library
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['image','title','description','year_of_issue','libraries','author']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['picture','FirstName','LastName','birthdate','deathdate','aboutAuthor']

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['image','name','address','phone','description']