from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('newDojo', views.newDojo),
    path('newNinja', views.newNinja),
    path('<_id>', views.delete),
]