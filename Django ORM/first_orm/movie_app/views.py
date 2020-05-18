from django.shortcuts import render
from .models import Movie

# Create your views here.
def first_view(request):
    context = {
        'all_the_movies': Movie.objects.all()
    }
    return render(request, 'index.html', context)

def second_view(request):
    context = {
        'data': [1, 2, 3]
    }
    return render(request, 'other_template.html', context)