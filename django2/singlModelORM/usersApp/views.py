from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    context = {
        "Uesr":User.objects.all()
    }
    return render(request, "index.html", context)