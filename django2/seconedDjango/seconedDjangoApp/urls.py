from django.urls import path     
from . import views
urlpatterns = [
    path('', views.start),
    path('time_display/', views.index),
]