from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  
    # path('<slug>/',name='tribe_detail'),
    path('test2/',test2_view,name='tribe_detail'),
    path('bokaro/',district_view,name='tribe_detail'),
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)