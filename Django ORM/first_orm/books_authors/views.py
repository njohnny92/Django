from django.shortcuts import render
from .models import Author, Book

# Create your views here.
def index(request):
    context = {'authors': Author.objects.all()}
    return render(request, 'book_author_index.html', context)