from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def feedback(request):
    with open("feedback/assets/feedback.html") as file:
        return HttpResponse(file.read())


def feedback_js(request):
    with open("feedback/assets/feedback.js") as file:
        return HttpResponse(file.read(), content_type='text/javascript')


def feedback_message(request):
    body = {"id": 123456}


def camera_feed(request):
    with open("mainMenu/assets/camDemo.mp4", "rb") as file:
        return HttpResponse(file.read(), content_type="video/mp4")
