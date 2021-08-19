from django.urls import path
from . import views

urlpatterns = [
    path("", views.feedback, name="feedback"),
    path("camFeed", views.camera_feed, name="camFeed"),
]