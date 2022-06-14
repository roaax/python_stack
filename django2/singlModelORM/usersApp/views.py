from multiprocessing import context
from django.shortcuts import render, redirect , HttpResponse
from flask import redirect
from .models import *

# Create your views here.
def index(request):
    users= User.objects.all()
    context={
        'users':users
    }

    return render(request, "index.html" , context)

def create(request):
    if request.methode =='POST':
        newUser = User.objects.create(
            fname=request.POST['fname'],
            lname=request.POST['lname'],
            email=request.POST['email'],
            age=request.POST['age'],
        )
        newUser.save()
    return redirect('/')
