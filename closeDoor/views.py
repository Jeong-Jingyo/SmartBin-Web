import sys
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DoorSerializer
from .models import Door
import json
import importlib
sys.path.append("/home/sqidward/dev/SmartBin")
HW = importlib.import_module("SmartBin-HardWare")


# Create your views here.
class DoorView(APIView):
    def get(self, request):
        return Response("ok", status=200)

    def post(self, request):
        serializer = DoorSerializer(data=request.data)
        if serializer.is_valid():
            HW.door(serializer.data["open"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class DoorClosedView(APIView):
    def get(self, request):
        body = {}
        body["closed"] = HW.door_closed()
        return Response(json.dumps(body), status=200, content_type="text/json")