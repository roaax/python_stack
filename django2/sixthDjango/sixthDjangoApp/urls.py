from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('process_money',views.process_money),
    path('reset', views.reset),
]

