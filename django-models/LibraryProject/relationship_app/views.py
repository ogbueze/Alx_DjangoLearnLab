from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from .models import Book, Library
# Create your views here.


def index(request):
    return HttpResponse('this is my relationship app')

def books(request):
    books = Book.objects.all()

    output = []
    for book in books:
        output.append(f"{book.title} by {book.author.name}")

    return HttpResponse("\n".join(output))

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'