from django.shortcuts import render
from django.http import HttpResponse
from utilities import data


def index(request):
    return HttpResponse(data.h)
