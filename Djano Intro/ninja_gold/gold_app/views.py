from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    print('*' * 60)
    print('IN THE INDEX METHOD')
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
        print(request.session['total_gold'])
    return render(request, 'index.html')

def process(request):
    print("*" * 60)
    print('IN THE PROCESS METHOD')
    request.session['activities'] = []
    if request.POST['properties'] == 'farm':
        gold = random.randint(10, 21)
        request.session['total_gold'] += gold
        print('*' * 40)
        print('SESSION NAMED PROPERTY IS EQUAL TO FARM')
        print(request.POST['properties'])
        data = {
            'property': request.POST['properties'],
            'sum_gold': gold
        }
        request.session['activities'].append(data)
    elif request.POST['properties'] == 'cave':
        gold = random.randint(5, 11)
        request.session['total_gold'] += gold
        print('*' * 40)
        print('SESSION NAMED PROPERTY IS EQUAL TO CAVE')
        print(request.POST['properties'])
        data = {
            'property': request.POST['properties'],
            'sum_gold': gold
        }
        request.session['activities'].append(data)
    elif request.POST['properties'] == 'house':
        gold = random.randint(2, 6)
        request.session['total_gold'] += gold
        print('*' * 40)
        print('SESSION NAMED PROPERTY IS EQUAL TO HOUSE')
        print(request.POST['properties'])
        data = {
            'property': request.POST['properties'],
            'sum_gold': gold
        }
        request.session['activities'].append(data)
    elif request.POST['properties'] == 'casino':
        gold = random.randint(-50, 51)
        request.session['total_gold'] += gold
        print('*' * 40)
        print('SESSION NAMED PROPERTY IS EQUAL TO CASINO')
        print(request.POST['properties'])
        if gold < 0:
            request.session['activities'].append(f"Entered a {request.POST['properties']} and lost {abs(gold)} gold...Ouch!")
        else:
            request.session['activities'].append(f"Earned {gold} golds from the {request.POST['properties']}!")
    return redirect('/')

def reset(request):
    del request.session['total_gold']
    return redirect('/')