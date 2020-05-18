from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.user_validations(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name = request.POST['firstname'], last_name = request.POST['lastname'], email=request.POST['email'], password=hashed_pw)
    return redirect('/')

def login(request):
    user = User.objects.filter(email = request.POST['email'])
    if not user:
        messages.error(request, 'Email does not exist.')
        return redirect('/')
    elif user is not None:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            request.session['user_firstname'] = logged_user.first_name
            request.session['user_lastname'] = logged_user.last_name
            return redirect('/books')
        else:
            messages.error(request, 'Invalid password.')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def book_index(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Please log into a registered account.')
        return redirect('/')
    context = {
        'all_books': Book.objects.all()
    }
    return render(request, 'create.html', context)

def add_books(request):
    Book.objects.create(title=request.POST['title'], desc)
    return redirect('/books')

def show_book(request):
    return render(request, 'show.html')

def edit_book(request):
    return render(request, 'edit.html')