from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='schoolmap'),
    re_path(r'^upload', views.uploadImg),
    re_path(r'^show', views.showImg),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
