from django.shortcuts import render, redirect

def index(request):
    #this method is to specifically render the html page with the form input submissions
    return render(request, 'index.html')

def create_user(request):
    #this method is to process the inputs from the form
    print("*" * 60)
    print("GOT INTO THE POST METHOD")
    request.session['user_name'] = request.POST['name']
    request.session['user_email'] = request.POST['email']
    return redirect('/success')

def success(request):
    #this is to render the success route
    data = {
        'name_on_template': request.session['user_name'],
        'email_on_template': request.session['user_email']
    }
    return render(request, 'show.html', data)