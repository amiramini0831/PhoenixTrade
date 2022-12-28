from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.main.models import *
from apps.main.forms import *
from apps.main.serializers import *


def media_admin(request):
    return {'meida_url':settings.MEDIA_URL}
# -------------------------------------------


def index(request):
  
    return render(request,'main.html')