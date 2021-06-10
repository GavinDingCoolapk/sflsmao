from django.shortcuts import render
from .models import IMG
from django.http import HttpResponse

def showImg(request):
    imgs = IMG.objects.all()
    content ={
        'imgs':imgs,
    }
    return render(request,'schoolmap/showimg.html',content)