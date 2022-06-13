from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),
    path('register/', views.register),
    path('login/', views.login),
    path('users/new/', views.new),
    path('users/', views.users),
]