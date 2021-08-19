import sys
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DoorSerializer
from .models import *
import cv2
import requests
import usr_cfg
import json
import importlib

sys.path.append("/home/sqidward/dev/SmartBin")
HW = importlib.import_module("SmartBin-HardWare")
cam = cv2.VideoCapture(0)


def capture():
    ret, frame = cam.read()
    yield frame



# Create your views here.
class DoorView(APIView):
    def get(self, request):
        return Response("ok", status=200)

    def post(self, request):
        serializer = DoorSerializer(data=request.data)
        if serializer.is_valid():
            HW.door(serializer.data["open"])
            if HW.door_closed() is True:
                image = capture()
                string_image = cv2.imencode(".jpg", image)[1].tostring()
                bytes_image = cv2.imencode(".jpg", image)[1]
                body = {"file": string_image}

                response = requests.post(usr_cfg.Backend_URL, body).json()
                max_class = max(response["trashType"], key=response["trashType"].get)


                foreign_subst = list()
                foreign_subst_probability = list()
                for i in range(len(response["foreignSubst"])):
                    foreign_subst.append(response["foreignSubst"][i][0])
                    foreign_subst_probability.append(response["foreignSubst"][i][1])

                trash_q = Trash(type=max_class,
                                type_probability=response["trashType"][max_class],
                                foreign_subst=",".join(foreign_subst),
                                foreign_subst_probability=",".join(foreign_subst_probability),
                                image=bytes_image
                                )
                trash_q.save()
                if int(max(response["trashType"], key=response["trashType"].get)) <= 0.8:
                    return Response(json.dumps({"ID": trash_q.id, "Result": "feedback"}))
                else:
                    return Response(json.dumps({"ID": trash_q.id, "Result": "tutorial"}))


class DoorClosedView(APIView):
    def get(self, request):
        body = dict()
        body["closed"] = HW.door_closed()
        return Response(json.dumps(body), status=200, content_type="text/json")
