from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from .forms import UploadFileForm

# Create your views here.
# Para - request: thong tin nhan tu server
def fileUploaderView (request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload(request.FILES['file'])
            return HttpResponse('<h2 style = \"color: blue\"> Upload file thanh cong </h2>')
        else:
            return HttpResponse('<h2 style = \"color: red\"> Upload file khong thanh cong </h2>')

    form = UploadFileForm()
    return render(request, 'fileUploadTemplate.html', { 'form':form })

# Thực hiện copy file vào thư mục gốc của server 
def upload(f):
    file = open(f.name, 'wb+')
    for chunk in f.chunks():
        file.write(chunk)