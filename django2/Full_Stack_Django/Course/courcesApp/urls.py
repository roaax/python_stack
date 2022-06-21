from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('add_course/',views.add_course),
    path('go_remove/<int:_id>/', views.go_remove),
    path('remove_course/<int:_id>/',views.remove_course),

]