from multiprocessing import context
from django.shortcuts import render, redirect , HttpResponse
from .models import *

# Create your views here.
def index(request):
    users= User.objects.all()
    context={
        'users':users
    }

    return render(request, "index.html" , context)

def create(request):
    if request.method =='POST':
        newUser = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email_address=request.POST['email_address'],
            age=request.POST['age'],
        )
        newUser.save()
    return redirect('/')
