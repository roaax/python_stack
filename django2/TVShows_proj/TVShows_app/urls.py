from django.urls import path
from . import views

urlpatterns = [
    path("",views.addShow),
    path("shows/new",views.addShow),
    path("shows/create",views.createShow),
    path("shows/<int:show_id>", views.show_info),
    path("shows/<int:show_id>/delete", views.deleteShow),
    path("shows", views.allShows),
    path("shows/<int:show_id>/edit", views.editShow),
    path("shows/<int:show_id>/update", views.updateShow),
]