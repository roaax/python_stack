
from django.urls import path     
from . import views
urlpatterns = [
    path('' , views.surveys),
    path('new/' , views.new),

]