from django.shortcuts import render, redirect, HttpResponse
from .models import Show
from django.contrib import messages

# Render Methods
def index(request):
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

def render_create(request):
    return render(request, 'create.html')

def render_read(request, show_id):
    this_show = Show.objects.get(id=show_id)
    context = {
        'read_show': this_show
    }
    return render(request, 'read.html', context)

def render_update(request, show_id):
    this_show = Show.objects.get(id=show_id)
    context = {
        'update_show': this_show
    }
    return render(request, 'update.html', context)

# Process Methods
def process_create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        Show.objects.create(title=request.POST['title'], network=request.POST['net'], description=request.POST['desc'], release=request.POST['release'])
    return redirect('/shows')

def process_update(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/' +str(show_id)+ '/edit')
    else:
        this_show = Show.objects.get(id = show_id)
        this_show.title=request.POST['title']
        this_show.network=request.POST['net']
        this_show.description=request.POST['desc']
        this_show.release=request.POST['release']
        this_show.save()
        messages.success(request, 'Show has successfully been updated!')
        return redirect('/shows/' +str(show_id)+'/edit')

def process_delete(request, show_id):
    this_show = Show.objects.get(id= show_id)
    this_show.delete()
    return redirect('/shows')