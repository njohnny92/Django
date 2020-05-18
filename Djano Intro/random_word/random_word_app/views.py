from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    print("*" * 60)
    generate_random = get_random_string(length=14)
    if 'visit' not in request.session:
        request.session['visit'] = 1
        request.session['random_word'] = generate_random
    else:
        request.session['visit'] += 1
        request.session['random_word'] = generate_random
    return render(request, 'index.html')

def delete(request):
    del request.session['visit']
    return redirect('/')