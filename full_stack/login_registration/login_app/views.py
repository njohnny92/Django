from django.shortcuts import render, redirect
import bcrypt
from .models import User
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout


# Render Methods
def index(request):
    return render(request, 'index.html')

# Process Methods
def process_register(request):
    errors = User.objects.user_validations(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        User.objects.create(first_name=request.POST['firstname'],last_name=request.POST['lastname'],email=request.POST['email'], password=hashed_pw)
    return redirect('/')

def process_login(request):
    user = User.objects.filter(email=request.POST['email'])
    if not user:
        messages.error(request, 'Email account does not exist!')
        return redirect('/')
    elif user is not None:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            request.session['user_fullname'] = logged_user.first_name + ' ' + logged_user.last_name
            return redirect('/success')
        else:
            messages.error(request, 'Invalid Password!')
    return redirect('/')

def process_logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Please Log-in to view the success page.')
        return redirect('/')
    return render(request, 'success.html')