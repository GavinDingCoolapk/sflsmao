from django.shortcuts import render
from .models import IMG
from django.http import HttpResponse
from django.urls import reverse


def index(request):
    s = "<a href='" + reverse("weatherdata") + "'>" + "天气实时数据</a><br/>" +\
        "<br><img src='/static/wholemap.png' alt='no picture'><br/>" +\
        "<a href='" + reverse("home") + "'>" + "返回首页</a>"
    return HttpResponse(s)


def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img')
        )
        new_img.save()
    return render(request, 'schoolmap/templates/uploadimg.html')


def showImg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs': imgs,
    }
    return render(request, 'schoolmap/templates/showimg.html', content)

