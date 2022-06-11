from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('result', views.result),
    path('goBack', views.goBack),

]

