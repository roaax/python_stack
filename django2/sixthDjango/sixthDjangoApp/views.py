from django.shortcuts import render, redirect
import random
from datetime import datetime

def root(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    context = {
        'gold': request.session['gold'],
        'activities': request.session['activity'],
        }
    return render(request,'index.html',context)
def process_money(request):
        if 'farm' in request.POST:
            _box = 'Farm'
            _random = random.randint(10,20)
        if 'cave' in request.POST:
            _box = 'Cave'
            _random = random.randint(10,20)
        if 'house' in request.POST:
            _box = 'House'
            _random = random.randint(10,20)
        if 'quest' in request.POST:
            _box = "Quest"
            _random = random.randint(-50,50)

        request.session['gold'] = request.session['gold'] + _random 

        if _random < 0:
            message = 'You failed a '+ _box + ' and lost ' + str(_random*-1) + ' gold.....Ouch'+ datetime.now().strftime('(%Y/%m/%d | %-I:%M %p)')
        else:
            message = 'You entered a '+ _box + ' and earned ' + str(_random) + ' gold' + datetime.now().strftime('(%Y/%m/%d | %-I:%M %p)')

        request.session['activity'].append(message)
        return redirect('/')

def reset(request):
    del  request.session['gold']
    del  request.session['activity']
    return redirect('/')