from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("main", views.main, name="main"),
    path("main.js", views.js, name="main.js"),
    path("stat.jpg", views.stat, name="stat.jpg"),
    path("tutorial", views.tutorial, name="tutorial"),
    path("tutorial.mp4", views.tuto_video, name="tutoVideo"),
    path("tutorial.js", views.tuto_js)
]
