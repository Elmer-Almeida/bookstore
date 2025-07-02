from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView

from .forms import CreateBookForm
from .models import Book


class BooksListView(ListView):
    model = Book
    queryset = Book.objects.all()
    template_name = 'store/books/list.html'
    context_object_name = 'books'


class BookCreateView(CreateView):
    model = Book
    form_class = CreateBookForm
    template_name = 'store/books/create.html'
