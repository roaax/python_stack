from django.shortcuts import render
from time import gmtime, strftime
    

def index(request):
    context = {
        "day" : strftime("%b %d, %Y", gmtime()),
        "time": strftime(" %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)

def start(request):
    return render(request , "index.html" )
