
from django.urls import *
from . import views

urlpatterns=[
    path('',views.index),
    path('register',views.register),
    path('login',views.login),
    path('show',views.book_index),
    path('logout',views.logout),
    path('addbook',views.add_book),
    path('likebook/<book_id>',views.like_book),
    path('show/<int:book_id>',views.show_book),
    path('unlikebook/<book_id>',views.unlike_book),
    path('update_book/<book_id>',views.update_book),
    path('delete_book/<book_id>',views.delete_book),
]