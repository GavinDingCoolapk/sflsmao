from django.shortcuts import render
from .models import IMG
from django.http import HttpResponse

def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img')
        )
        new_img.save()
    return render(request, 'schoolmap/uploadimg.html')
