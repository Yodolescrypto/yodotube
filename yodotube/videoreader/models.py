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
            hash = api.add(fd);
            api.pin(hash);
        except ipfshttpclient.exceptions.ConnectionError as ce:
            print("Upload Error:". str(ce));

    def listVideo():
        try:
            api = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001");
        except ipfshttpclient.exceptions.ConnectionError as ce:
            print("CACA".str(ce));
        videolist = api.pin.ls(type="recursive");
        videolist = videolist.as_json().values();
        hashlist = [];
        for i in videolist:
            for v in i:
                hashlist.append(v);
        return hashlist;

    def getVideo(hash):
        try:
            api = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5001");
        except ipfshttpclient.exceptions.ConnectionError as ce:
            print("CACA".str(ce));

        print(hash);
        api.get(hash);
        os.rename(os.path.basename(hash), "static/videos/"+hash);
        return (hash);