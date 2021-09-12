import sys
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
import cv2
import requests
import usr_cfg
import json
import importlib
import io
import asyncio

sys.path.append("C:\\Users\\sqidw\\dev\\SmartBin\\SmartBin-Web\\SmartBin")
HWLib = importlib.import_module("SmartBin-Hardware")
HW = HWLib.Serial()
# asyncio.run(HW.get_stat)
HWMap = {
    "pet": HW.bin1,
    "pet-re": HW.bin2,
    "plastic": HW.bin3,
    "glass": HW.bin4,
    "glass-re": HW.bin5,
    "can": HW.bin6,
    "other": HW.bin7,
    "dynamic": HW.bin8
}
cam = cv2.VideoCapture(0)
cam.read()


def capture():
    ret, frame = cam.read()
    return frame


# Create your views here.
class DoorView(APIView):
    def get(self, request):
        return Response("ok", status=200)

    def post(self, request):
        serializer = DoorSerializer(data=request.data)
        if serializer.is_valid():
            HW.door()
            if HW.is_closed():
                image = capture()
                encoded_image = cv2.imencode(".jpg", image)[1]

                buffer = io.BytesIO(encoded_image.tobytes())

                response = requests.post(usr_cfg.Backend_URL + '/ai', files={"file": buffer})
                response = response.json()
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
                                feedback_type="",
                                )
                trash_q.save()
                img_dir = os.path.abspath("data/TrashImages/" + str(trash_q.id) + ".jpg")
                cv2.imwrite("data/TrashImages/" + str(trash_q.id) + ".jpg", image)
                trash_q.image = img_dir
                trash_q.save()
                with open("test.jpg", "wb") as file:
                    file.write(buffer.read())

                if float(response["trashType"][max_class]) <= 0.8:
                    return Response(json.dumps({"ID": trash_q.id, "Result": "feedback"}))
                else:
                    if not bool(foreign_subst):
                        HWMap[max_class]()
                    elif max_class == "pet":
                        HWMap["pet-re"]()
                    elif max_class == "glass":
                        HWMap["glass-re"]()
                    return Response(json.dumps({"ID": trash_q.id, "Result": "tutorial"}))


class DoorClosedView(APIView):
    def get(self, request):
        body = dict()
        body["closed"] = HW.is_closed()
        return Response(json.dumps(body), status=200, content_type="text/json")


class EndView(APIView):
    def get(self, request):
        return Response(json.dumps({"done": HW.is_done()}), status=200)


class FeedBackView(APIView):
    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            t_type = serializer.data["feedback_type"]
            t_foreign = serializer.data["feedback_foreign_subst"]
            trash_id = request.GET.get("ID")
            trash_q = Trash.objects.get(id=trash_id)
            trash_q.feedback_type = t_type
            trash_q.feedback_foreign_subst = t_foreign
            trash_q.save()
            if t_type in ["glass", "pet"] and t_foreign:
                HWMap[t_type + "-re"]()
            else:
                HWMap[t_type]()
            return Response(json.dumps({"Result": True}), status=201)
        else:
            return Response(json.dumps({"Result": False}), status=400)


class TerminatorView(APIView):
    def post(self, request):
        serializer = TerminateSerializer(data=request.data)
        if serializer.is_valid():
            HW.terminate()
        return Response(json.dumps({"Result": True}), status=200)
