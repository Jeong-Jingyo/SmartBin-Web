from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
import io
from api.models import Trash
import base64


# Create your views here.
def index(request):
    with open("mainMenu/assets/index.html", encoding='utf-8') as file:
        return HttpResponse(file.read())

def main(request):
    with open("mainMenu/assets/main.html", encoding='utf-8') as file:
        return HttpResponse(file.read())

def js(request):
    with open("mainMenu/assets/mainMenu.js", encoding='utf-8') as file:
        return HttpResponse(file.read(), content_type='text/javascript')


def stat(request):
    wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}
    data = count_type()
    data = {key: val for key, val in data.items() if val != 0}
    plt.pie(data.values(), labels=data.keys(), wedgeprops=wedgeprops)
    b = io.BytesIO()
    plt.savefig(b, format='jpg', dpi=600)
    b.seek(0)
    return HttpResponse(b.read(), content_type="image/image")


def count_type():
    can = general = glass = paper = pet_bottle = pet_coffee = plastic = 0

    classfied = Trash.objects.all()
    can += classfied.filter(type="can").count()
    general += classfied.filter(type="general").count()
    glass += classfied.filter(type="glass").count()
    paper += classfied.filter(type="paper").count()
    pet_bottle += classfied.filter(type="pet_bottle").count()
    pet_coffee += classfied.filter(type="pet_coffee").count()
    plastic += classfied.filter(type="plastic").count()
    print((can, general, glass, paper, pet_bottle, pet_coffee, plastic))

    return {"Can": can, "General": general, "Glass": glass, "Paper": paper,
            "Pet": pet_bottle, "Take-out\nCup": pet_coffee, "Plastic": plastic}


def tutorial(request):
    with open("mainMenu/assets/tutorial.html", encoding='utf-8') as file:
        return HttpResponse(file.read())


def tuto_video(request):
    with open("mainMenu/assets/tutorial.mp4", "rb") as file:
        return HttpResponse(file.read(), content_type="video/avi")


def tuto_js(request):
    with open("mainMenu/assets/tutorial.js", encoding="utf-8") as file:
        return HttpResponse(file.read(), content_type="application/javascript")
