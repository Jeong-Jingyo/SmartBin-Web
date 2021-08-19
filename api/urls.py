from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('/door', views.DoorView.as_view()),
    path('/closed', views.DoorClosedView.as_view())
]
