from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('root', views.root),
    path('playAgain', views.playAgain)
]