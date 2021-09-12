from django.shortcuts import render
from django.http import HttpResponse
from api.models import Trash


# Create your views here.
def feedback(request):
    ID = int(request.GET.get("ID"))
    with open("feedback/assets/feedback.html", encoding='utf-8') as file:
        return HttpResponse(file.read().format(id=ID))


def feedback_js(request):
    with open("feedback/assets/feedback.js", encoding='utf-8') as file:
        return HttpResponse(file.read(), content_type='text/javascript')


def camera_feed(request):
    ID = int(request.GET.get("ID"))
    img_dir = Trash.objects.get(id=ID).image
    with open(img_dir, "rb") as file:
        return HttpResponse(file.read(), content_type="image/jpg")
