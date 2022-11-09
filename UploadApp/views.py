from django.shortcuts import render
from django.http import HttpResponse
from .task import *
 

# Create your views here.
def index(request):
    if request.method == 'POST':
        # file_name = request.POST['filename']
        files = request.FILES.getlist('files')
        file_upload(files)
        return render(request, 'UploadApp/uploading.html')
    return render(request, 'UploadApp/index.html')

def uploading(request):
    return render(request, 'UploadApp/uploading.html')
