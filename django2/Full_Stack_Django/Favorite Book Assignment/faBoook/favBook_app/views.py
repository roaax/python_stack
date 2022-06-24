from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

#  -----------First page -------------
def index(request):
    return render(request, 'index.html')

# --------------- Register in first page & validation
def register(request):
    if request.method == 'POST':
        errors = User.objects.register_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            hash_pass = bcrypt.hashpw(
                request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                fname=request.POST['fname'],
                lname=request.POST['lname'],
                email=request.POST['email'],
                birthday=request.POST['birthday'],
                password=hash_pass
            )
            user.save()
            messages.success(request, "User successfully added!")

            request.session['user_id'] = user.id
            return redirect('/show')
    return redirect('/')

# --------------- Register in first page & validation
def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            userid = User.objects.get(email__iexact=request.POST['email'])
            request.session['user_id'] = userid.id
            return redirect('/show')

    return redirect('/')

# ------------- book page
def book_index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'books': Book.objects.all(),
    }
    return render(request, 'show_book.html', context)


def logout(request):
    del request.session['user_id']
    return redirect('/')


def add_book(request):
    if request.method == 'POST':
        errors = Book.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/show")
        else:
            user = User.objects.get(id=request.session['user_id'])
            book = Book.objects.create(
                title=request.POST['title'],
                description=request.POST['description'],
                uploaded_by=user,
            )

            messages.success(request, "Book successfully added!")
        return redirect('/show')
    return redirect('/show')

# -------- click on like btn
def like_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['user_id'])

    book.users_who_like.add(user)
    book.save()

    # back to the previous link
    return redirect(request.META.get('HTTP_REFERER'))

#  we send user& book info to show the book info on another page 
def show_book(request, book_id):
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "book": Book.objects.get(id=book_id)
    }

    return render(request, 'books_index.html', context)

# -------- click on unlike btn
def unlike_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['user_id'])

    book.users_who_like.remove(user)
    book.save()

    # back to the previous link
    return redirect(request.META.get('HTTP_REFERER'))

# we check if u send a post requesst then we replace book info with the information u send 
def update_book(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        errors = Book.objects.book_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/show/{book_id}")
        else:
            book.title = request.POST['title']
            book.description = request.POST['description']
            book.save()

            messages.success(request, "Book successfully updated!")
            return redirect(f'/show/{book_id}')

#   ---------- when we click on delete btn  
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if book.uploaded_by.id == request.session['user_id']:
        book.delete()

    return redirect('/show')

