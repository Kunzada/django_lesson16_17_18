from django import forms 
from .models import Book,Author,Library
from captcha.fields import CaptchaField
class BookForm(forms.ModelForm):
    captcha=CaptchaField(generator='captcha.helpers.random_char_challenge')
    class Meta:
        model = Book
        fields = ['image','title','description','year_of_issue','libraries','author']

class AuthorForm(forms.ModelForm):
    captcha=CaptchaField(generator='captcha.helpers.word_challenge')
    class Meta:
        model = Author
        fields = ['picture','FirstName','LastName','birthdate','deathdate','aboutAuthor']

class LibraryForm(forms.ModelForm):
    captcha=CaptchaField(generator='captcha.helpers.math_challenge')
    class Meta:
        model = Library
        fields = ['image','name','address','phone','description']