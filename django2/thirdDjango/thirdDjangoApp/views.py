from multiprocessing import context
from django.shortcuts import render, redirect # don't forget to import redirect!

def index(request):
    # this is the route that shows the form
    return render(request,"index.html")

def result(request):
    # this is the route that shows the form
    name_from_form = request.POST['name']
    location_from_form = request.POST['dojoLocation']
    favLanguage_from_form = request.POST['favLanguage']
    comment_from_form = request.POST['comment']

    context = {
        "name_on_template" : name_from_form,
        "location_on_template" : location_from_form,
        "favLanguage_on_template" : favLanguage_from_form,
        "comment_on_template" : comment_from_form
    }
    return render(request,"result.html" , context)

def goBack(request):
    GoBack = request.POST['goBack']
    context={
        "goBack": GoBack
    }
    return render(request , "index.html" , context)
