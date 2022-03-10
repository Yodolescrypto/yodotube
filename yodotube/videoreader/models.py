from django.db import models
import requests
import json, statistics, ipfshttpclient, os
from django import forms

# Create your models here.

class UploadModel(models.Model):
    def uploadVideo(video, title):
        fd = os.path.basename(str(title));
        with open(fd, 'wb+') as destination:
            for chunk in video.chunks():
                destination.write(chunk);
        try:
            api = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001");
        except ipfshttpclient.exceptions.ConnectionError as ce:
            print("CACA".str(ce));
        
        try:
            api.add('akaka');
        except ipfshttpclient.exceptions.ConnectionError as ce:
            print("Upload Error:". str(ce));