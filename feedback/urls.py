from django.urls import path
from . import views

urlpatterns = [
    path("", views.feedback, name="feedback"),
    path("/feedback.js", views.feedback_js, name="feed.js"),
    path("/camFeed", views.camera_feed, name="camFeed"),
]