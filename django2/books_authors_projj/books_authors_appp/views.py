
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request,'index.html',context)

# Creat new book to table
def addBook(request):
        if request.method=='POST':
            _addBook= Book.objects.create(
                title=request.POST['title'],
                desc=request.POST['desc'],
            )
            _addBook.save()
        return redirect('/')

def delete(request, _idBook):
    book = Book.objects.get(id=_idBook)
    book.delete()
    return redirect('/')

def goAuthor(request):
    return redirect('/authors')


def author(request):
    authors = Author.objects.all()
    context = {
        'authors':authors
    }
    return render(request,'authors.html',context)

# Creat an author and add it to th table
def addAuthor(request):
        if request.method=='POST':
            _addAuthor= Author.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                notes=request.POST['notes'],     
            )
            _addAuthor.save()
        return redirect('/authors')

#new page with ALL information of Book [books path]
def book_info(request , book_id):
    context={
        "book":Book.objects.get(id=book_id),
        "authors":Author.objects.all()
    }
    return render(request, 'book_info.html' , context)

# Add author to the book in page 2
def addAuthorToBook(request, book_id):
    book= Book.objects.get(id=book_id)
    author= Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    
    return redirect(f"/books/{book_id}")

#new page with ALL information of Author [authors path]
def author_info(request, author_id):
    context={
        "author": Author.objects.get(id=author_id),
        "books": Book.objects.all()    
    }
    return render(request, "author_info.html", context)


def addBookToAuthor(request, author_id):
    author= Author.objects.get(id=author_id)
    book= Book.objects.get(id=request.POST['book_id'])
    author.books.add(book)
    
    return redirect(f"/authors/{author_id}")

def delete_author(request, _idAuthor):
    author = Author.objects.get(id=_idAuthor)
    author.delete()
    return redirect('/authors')

# 
#                 
# 

