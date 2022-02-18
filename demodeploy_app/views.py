import csv
from datetime import date
# from genericpath import exists
from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from demodeploy.settings import *
from django.core.files.storage import FileSystemStorage
import os
#import pandas as pd
import datetime
import calendar


class index(APIView):
    def post(self,request):
        getname=request.data["name"]
        print(getname)
        return Response(getname)
    def get(self,request):
        return Response('get')

class web(APIView):
    def post(self,request):
        return HttpResponse('post')
    def get(self,request):
        return HttpResponse('getting the data')