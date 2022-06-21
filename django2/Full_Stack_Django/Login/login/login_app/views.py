from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            newUser = User.objects.create(
                fname = request.POST['fname'],
                lname = request.POST['lname'],
                email = request.POST['email'],
                password = hash
            )
            newUser.save()
            messages.success(request,"User successfully added!")

            request.session['user_id'] = newUser.id
            return redirect('/success')
    return redirect('/')


def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            request.session['user_id'] = User.objects.get(email=request.POST['email']).id
            return redirect('/success')

    return redirect('/') 

def success(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        "user" : User.objects.get(id=request.session['user_id']),
    }
    return render(request, "success.html", context)

def signout(request):
    del request.session['user_id']
    return redirect("/")

# ---------------------------------------

