from django.shortcuts import render

import json
from django.http import HttpResponseRedirect, HttpResponse
from .models import UploadModel
from .forms import UploadForm

# Create your views here.

def index(request):
    return render(request, 'index.html');
    
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES);
        if form.is_valid():
            UploadModel.uploadVideo(request.FILES['file'], request.POST['title']);
            return render(request, 'upload.html');
        else:
            print(request.POST);
            return HttpResponse('caca');
    else:
        form = UploadForm();
        return render(request, 'upload.html', {'form': form});
def stream(request):
    videos = UploadModel.listVideo();
    print(videos)
    return render(request, 'list.html', {'videos': videos});