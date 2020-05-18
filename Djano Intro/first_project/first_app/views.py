from django.shortcuts import render, HttpResponse, redirect

def index(request):
    dictionary = {
        "name" : "Johnny",
        "fav_color" : "black",
        "pets" : ["Bubbles", "Inori"]
    }
    return render(request, "index.html", dictionary)