from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        file_name = request.POST['filename']
        files = request.FILES.getlist('files')
        print(file_name, files)
        return HttpResponse('Done')
    return render(request, 'UploadApp/index.html')

