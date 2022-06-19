from django.urls import path
from . import views
urlpatterns = [

    path('', views.index),
    path('addBook',views.addBook),
    path('books/<int:book_id>/',views.book_info),
    path('addAuthorToBook/<int:book_id>/', views.addAuthorToBook),
    path('deleteBook/<_idBook>/',views.delete), 

    path('authors/',views.author),
    path('addAuthor',views.addAuthor),
    path('authors/<author_id>/', views.author_info),
    path('addBookToAuthor/<int:author_id>/', views.addBookToAuthor),
    path('goAuthor/',views.goAuthor),
    path('delete_author/<_idAuthor>',views.delete_author),
]

# -------Add a Book Page----------
# index html: for book
# addBook html: to add new book to the table  in the same page

# -------Add an Author Page----------
# authors html: for authors page
# addAuthor html: to add new author to the table in same page

# -------Book information Page----------
# book_info html to show us all the information of the book you have viewed
# extraAuthor html  to (select an author) to add it to the book

# -------Authors information Page----------
# author_info html to show us a new page with all information about author you have been viewed
# extraBook html to (select a book) to add it to the author 