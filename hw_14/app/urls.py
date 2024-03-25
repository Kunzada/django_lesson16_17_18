from django.urls import path 
from .views import *

urlpatterns=[
    path('',LibraryList.as_view(),name='home'),
    path('detail/<int:pk>/',DetailLibrary.as_view(),name='detail'),
    path('search/',Search.as_view(),name='search'),
    path('book/<int:pk>/',DetailBook.as_view(),name='book'),
    path('author/<int:pk>/',DetailAuthor.as_view(),name='author'),
    path('createlibrary/',CreateLibrary.as_view(),name='create_library'),
    path('create_book/',CreateBook.as_view(),name='create_book'),
    path('create_author/',CreateAuthor.as_view(),name='create_author'),

]