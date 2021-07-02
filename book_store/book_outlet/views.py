from django.http import request
from django.shortcuts import get_object_or_404, render
from .models import Book

def query_books():
    books=Book.objects.all()
    return books

# Create your views here.

def index(request):
    all_books=query_books()
    return render(request,"book_outlet/index.html",{
        "books":all_books
    })

def book_detail(request,slug):
    # specific_book=Book.objects.get(slug=slug)
    specific_book=get_object_or_404(Book,slug=slug)
    return render(request,"book_outlet/book_detail.html",{
        "book":specific_book
    })
