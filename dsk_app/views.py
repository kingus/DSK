from django.shortcuts import render
from rest_framework.views import APIView, Response
from django.utils import timezone
import time

class InfoView(APIView):

    def get(self, request):
        time.sleep(10)

        return Response({"info": timezone.now()})