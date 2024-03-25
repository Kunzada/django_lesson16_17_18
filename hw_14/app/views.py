from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView ,DetailView,CreateView
from .models import *
from .forms import *

class LibraryList(ListView):
    model=Library 
    template_name='home.html'
    # context_object_name='libraries'
    paginate_by = 2

class DetailLibrary(DetailView):
    model=Library
    template_name='detail.html'
    context_object_name='library'
    
    def get_context_data(self, **kwargs) :
        context= super().get_context_data(**kwargs)
        context['books']=Book.objects.filter(libraries=self.object)
        return context
    


class Search(ListView):
    template_name='home.html'
    context_object_name='libraries'
    paginate_by=5

    def get_queryset(self):
        return Library.objects.filter(name__icontains=self.request.GET.get('q'))
    
    def get_context_data(self, **kwargs: Any) :
        context= super().get_context_data(**kwargs)
        context['q']=self.request.GET.get('q')
        return context
    
class DetailBook(DetailView):
    model=Book 
    template_name="book.html"
    context_object_name='book'

    def get_context_data(self, **kwargs: Any) :
        context= super().get_context_data(**kwargs)
        # context['author']=Author.objects.filter(books=self.object)
        return context
    
class DetailAuthor(DetailView):
    model=Author 
    template_name="author.html"
    context_object_name='author'

    def get_context_data(self, **kwargs: Any) :
        context= super().get_context_data(**kwargs)
        context['books']=Book.objects.filter(author=self.object)
        return context
    
class CreateBook(CreateView):
    model=Book
    form_class=BookForm
    template_name="create_book.html"
    success_url=reverse_lazy('home')
class CreateAuthor(CreateView):
    model=Author
    form_class=AuthorForm
    template_name="create_author.html"
    success_url=reverse_lazy('home')

class CreateLibrary(CreateView):
    model=Library
    form_class=LibraryForm
    template_name="create_library.html"
    success_url=reverse_lazy('home')