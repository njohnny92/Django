from django.shortcuts import render, redirect
from .models import Author, Book

# Create your views here.
def index(request):
    context = {'books': Book.objects.all()}
    return render(request, 'index.html', context)

def author_table(request):
    context = {'authors': Author.objects.all()}
    return render(request, 'author.html', context)

def add_book(request):
    Book.objects.create(title=request.POST['title'], description=request.POST['desc'])
    return redirect('/')

def add_author(request):
    Author.objects.create(first_name=request.POST['firstname'], last_name=request.POST['lastname'], notes=request.POST['notes'])
    return redirect('/authors')

def show_book(request, book_id):
    this_book = Book.objects.get(id=book_id)
    authors = this_book.author.all()
    context = {
        'one_book': this_book,
        'books_authors': authors,
        'avaliable_authors': Author.objects.all()
        }
    return render(request, 'show_book.html', context)

def show_author(request, author_id):
    this_author = Author.objects.get(id=author_id)
    context = {
        'one_author': this_author,
#this_author shows the author with that specific id, and gets all the book objects that are within that author.
        'authors_books': this_author.books.all(),
        'avaliable_books': Book.objects.all()
    }
    return render(request, 'show_author.html', context)

def author_to_book(request, book_id):
    this_book = Book.objects.get(id=book_id)
    this_author = Author.objects.get(id=request.POST['author'])
    this_book.author.add(this_author)
    return redirect('/books/' + str(book_id))

def book_to_author(request, author_id):
    this_author = Author.objects.get(id=author_id)
    this_book = Book.objects.get(id=request.POST['book'])
    this_author.books.add(this_book)
    return redirect('/authors/'+str(author_id))