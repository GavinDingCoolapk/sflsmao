from django.conf.urls import url
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='schoolmap'),
] + [url(r'^upload', views.uploadImg, name='schoolmap'),
     url(r'^show', views.showImg, name='schoolmap')
     ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
