from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from . import data


def index(request):
    s = data.h +\
        "<a href='" + reverse("home") + "'>" + "返回首页</a>" + \
        "<a href='" + reverse("schoolmap") + "'>" + "学校地图</a>"
    return HttpResponse(s)