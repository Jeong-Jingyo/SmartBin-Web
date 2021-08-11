from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import cv2
import io


# Create your views here.
def index(request):
    with open("mainMenu/assets/index.html") as file:
        return HttpResponse(file.read())


def js(request):
    with open("mainMenu/assets/main.js") as file:
        return HttpResponse(file.read(), content_type='text/javascript')


def stat(request):
    plt.subplots(nrows=1, ncols=1, figsize=(8, 8))
    plt.pie([1, 2, 3, 4])  # todo: DB와 연결
    plt.tight_layout()
    b = io.BytesIO()
    plt.savefig(b, format='jpg')
    b.seek(0)
    return HttpResponse(b.read(), content_type="text/image")


def feedback(request):
    with open("mainMenu/assets/feedback.html") as file:
        return HttpResponse(file.read())


def camera_feed(request):
    with open("mainMenu/assets/cameraFeed.mp4", "rb") as file:
        return HttpResponse(file.read(), content_type="video/mp4")
