from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *


# THe first page to add a new show
def addShow(request):
    return render(request , "index.html")

# btn
def createShow(request):
    if request.method=='POST':
            show= Show.objects.create(
                title=request.POST['title'],
                network=request.POST['network'],
                release_date=request.POST['release_date'],
                desc=request.POST['desc'],
            )
            show.save()
    return redirect(f"/shows/{show.id}")

# after click btn we are going to this show info page
def show_info(request, show_id):
    context ={
        "nShow":Show.objects.get(id=show_id)
    }
    return render(request, "show_info.html", context)

# delete linke in show info page  /i have to check it befor submit
def deleteShow(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect("/shows")

#page of table with all shows
def allShows(request):
    context ={
        "shows":Show.objects.all()
    }
    return render(request,"all_shows.html", context )

#Edit page 
def editShow(request, show_id):
    show=Show.objects.get(id=show_id)
    show.release_date = show.release_date.strftime("%Y-%m-%d")
    context = {
        "show" : show
    }

    return render(request, "edit_show.html", context)


# btn update show
def updateShow(request, show_id):
    if request.method=='POST':
        updateShow= Show.objects.get(id=show_id)
        updateShow.title= request.POST['title']
        updateShow.network=request.POST['network']
        updateShow.release_date=request.POST['release_date']
        updateShow.description=request.POST['desc']
        updateShow.save()
    return redirect(f'/shows/{show_id}')

