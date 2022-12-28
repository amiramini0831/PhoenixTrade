from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from apps.product.models import *
from apps.product.forms import *
from apps.product.serializers import *

