
from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),
    path('surveys/' , views.surveys),
    path('surveys/new/' , views.new),

]