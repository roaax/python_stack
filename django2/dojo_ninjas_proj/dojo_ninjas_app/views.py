from django.shortcuts import render,redirect
from .models import*
# Create your views here.
def index(request):
    dojos = Dojos.objects.all()
    ninjas = Ninjas.objects.all()
    context ={
        'dojos':dojos,
        'ninjas':ninjas
    }
    return render(request,'index.html',context)

def newDojo(request):
    if request.method == 'POST':
        newDojo = Dojos.objects.create(
            name=request.POST['name'],
            city=request.POST['city'],
            state=request.POST['state'],
        )
        newDojo.save()
    return redirect('/')

def newNinja(request):
    if request.method == 'POST':
        newNinja = Ninjas.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            dojo_id=Dojos.objects.get(id=request.POST['dojo']),
        )
        newNinja.save()
    return redirect('/')

def delete(request, _id):
    dojo = Dojos.objects.get(id=_id)
    dojo.delete()
    
    return redirect('/')