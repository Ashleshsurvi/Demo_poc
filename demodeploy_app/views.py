import csv
from datetime import date
# from genericpath import exists
from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from demodeploy.settings import *
from django.core.files.storage import FileSystemStorage,default_storage
from django.core.files.base import ContentFile
import os
import pandas as pd
import datetime
import calendar
import PIL  
from PIL import Image  

class index(APIView):
    def post(self,request):
        f = request.FILES['file']
        filename=f.name
        name, extension = os.path.splitext(filename)
        img_path=str(BASE_DIR)+"/files/images/"+name
        if os.path.exists(img_path):
            print("yes")
        
        print(img_path)
        # print(name)
        # print(extension)

        extension=extension.replace(".",'')
        
        if extension.lower()=="jpeg" or extension.lower()=="jpg" or extension.lower()=="gif" or extension.lower()=="svg" or extension.lower()=="png" or extension.lower()=="tiff" or extension.lower()=="tif":
            picture = Image.open(f) 
            rgb_im = picture.convert("RGB")
            rgb_im.save(img_path+".tif")
            print("image")

        elif extension.lower()=="pdf" or extension.lower()=="doc" or extension.lower()=="docx" or extension.lower()=="html" or extension.lower()=="htm" or extension.lower()=="xls" or extension.lower()=="xlsx" or extension.lower()=="txt" or extension.lower()=="csv":
            print("document")



        return Response("success")
    
    
    
    def get(self,request):
        from datetime import datetime
        date1 = date.today()
        date2 = date(2022,3, 11)
        nodays=date2-date1
        nodays=nodays.days
        sentence_days=nodays
        if nodays==1:
            nodays=str(nodays)+"day "
        else:
            nodays=str(nodays)+"days "
        print(nodays)
        now = datetime.now()
        time_hr = int(now.strftime("%H"))
        time_hr=24-time_hr
        if time_hr==1:
            time_hr=str(time_hr)+"hr "
        else:
            time_hr=str(time_hr)+"hrs "
        time_min = int(now.strftime("%M"))
        time_min=60-time_min
        if time_min==1:
            time_min=str(time_min)+"min "
        else:
            time_min=str(time_min)+"min "
        time_sec = int(now.strftime("%S"))
        time_sec=60-time_sec
        if time_sec==1:
            time_sec=str(time_sec)+"sec "
        else:
            time_sec=str(time_sec)+"sec "
        
        print(type(time_sec))
        print(time_sec)
        
        if sentence_days>=1:
            sentence="ADVANCE HAPPY BIRTHDAY SANKEERTH MORE "+nodays+time_hr+time_min+time_sec+"TO GO"
        elif sentence_days==0:
            sentence="HAPPY BIRTHDAY SANKEERTH"
        elif sentence_days<0:
            sentence="BELATED HAPPY BIRTHDAY SANKEERTH"
        return Response(sentence)

class web(APIView):
    def post(self,request):
        return HttpResponse('post')
    def get(self,request):
        return HttpResponse('sample testing')