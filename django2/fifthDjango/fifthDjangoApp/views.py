from urllib import request
from urllib.request import Request
from django.shortcuts import render, redirect
import random 	                # import the random module

def index(request):
    return render(request, "index.html")

def root (request):
    root = ""  
    if request.POST['guess']:
        request.session['Random']= random.randint(1, 100)
        request.session['guess']= int(request.POST['guess'])
        request.session['button'] = False

        if (request.session['guess']< request.session['Random']):
            root = str(request.session['guess'] )+ " Too Low!!"
        elif(request.session['guess'] > request.session['Random']):
            root = str(request.session['guess'] )+ " Too High!!"
        else:
            root = str(request.session['guess'] )+ " Was The Number"
            request.session['button'] = True
        context = {
            "root" : root,
            "button" : request.session['button']
        }

    else:
        notGuess= " Pleas Guess a Number!"
        context={
            "notGuess" : notGuess
        }
    return render(request, "index.html", context)

def playAgain(request):
    return redirect('/')