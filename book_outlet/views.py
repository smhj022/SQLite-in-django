from django.shortcuts import render
from .models import Book
from django.http import Http404
from django.db.models import Avg

# Create your views here.


def index(request):
    books = Book.objects.all()
    no_of_book = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    print(avg_rating)
    return render(request, "book_outlets/index.html", {
        "books": books,
        "total_no_of_books": no_of_book,
        "average_rating": avg_rating
    })


def book_details(request, slug):
    try:
        book = Book.objects.get(slug=slug)
        return render(request, "book_outlets/book_details.html", {
            "book": book,
        })
    except:
        raise Http404
