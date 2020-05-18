from django.shortcuts import render, redirect
from .models import User, Message, Comment
import bcrypt
from django.contrib import messages, auth

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
        User.objects.create(first_name=request.POST['firstname'], last_name=request.POST['lastname'], email=request.POST['email'], password=hashed_pw)
    return redirect('/')

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if not user:
        messages.error(request, 'Email account does not exist.')
        return redirect('/')
    elif user is not None:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            request.session['user_fullname'] = logged_user.first_name + ' ' + logged_user.last_name
            return redirect('/wall')
        else:
            messages.error(request, 'Invalid password.')
    return redirect('/')

def logout(request):
    del request.session['user_id']
    del request.session['user_fullname']
    return redirect('/')

def wall(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Please log in to a registered account.')
        return redirect('/')
    context = {
        'message_posts': Message.objects.all(),
        'comment_posts': Comment.objects.all()
    }
    return render(request, 'wall.html', context)

def post_message(request):
    Message.objects.create(message=request.POST['post_message'], user=User.objects.get(id=request.session['user_id']))
    return redirect('/wall')

def post_comment(request):
    Comment.objects.create(
        comment = request.POST['post_comment'],
        user=User.objects.get(id=request.session['user_id']),
        message=Message.objects.get(id=request.POST['message_id'])
    )
    return redirect('/wall')

def delete_message(request, message_id):
    this_message = Message.objects.get(id=message_id)
    this_message.delete()
    return redirect('/wall')

def delete_comment(request, comment_id):
    this_comment = Comment.objects.get(id=comment_id)
    this_comment.delete()
    return redirect('/wall')
