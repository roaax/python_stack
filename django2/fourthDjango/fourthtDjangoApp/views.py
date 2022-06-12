
from django.shortcuts import render,redirect


def session(request):
    if 'counter' in request.session:
        request.session['counter']+=1
    else:
        request.session['counter'] =0
    return render(request,"index.html")

def destroy(request):
    del request.session['counter']
    return redirect('/')


def double(request):
    request.session['counter'] +=2
    return redirect('/')