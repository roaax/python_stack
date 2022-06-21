from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import Users



def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        errors = Users.objects.validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            pwHash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            newUser = Users.objects.create(fname=fname,lname=lname,email=email,password=pwHash)
            newUser.save()
            request.session['loggedInId'] = newUser.id
        return redirect('/success')
    else:
        return redirect('/')

def success(request):
    context = {
        'loggedInUser': Users.objects.get(id = request.session['loggedInId'])
    }
    return render(request, 'success.html', context)