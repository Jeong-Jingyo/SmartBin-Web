from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("main.js", views.js, name="main.js"),
    path("stat.jpg", views.stat, name="stat.jpg")
]
