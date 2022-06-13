from django.shortcuts import render,redirect,HttpResponse

def root(request):
    return redirect("/blogs")
def register(request):
    return HttpResponse("placeholder for users to create a new user record")
def login(request):
    return HttpResponse("placeholder for users to log in")
def new(request):
    return redirect("/register")
def users(request):
    return HttpResponse("placeholder to later display all the list of users")
