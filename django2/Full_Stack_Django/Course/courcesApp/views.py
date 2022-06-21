from itertools import count
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    context={
        'courses':Course.objects.all()
    }
    return render(request, 'index.html', context)

def add_course(request):
    if request.method=='POST':
        errors=Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            _newCourse=Course.objects.create(
                name=request.POST['name'],
                desc=request.POST['desc']
            )
            _newCourse.save()
            messages.success(request, "Successfully Added!")
        return redirect ('/')
    else:
        return redirect ('/')

def go_remove(request, _id):
    context={
        'course':Course.objects.get(id=_id)
    } 
    return render(request, 'remove.html', context)


def remove_course(request, _id):
    course = Course.objects.get(id=_id)
    course.delete()
    return redirect('/')




