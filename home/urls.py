from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view,name='home'),
    path('asur/',asur_view,name='asur'),
    path('test/',test_view,name='test'),
    path('form/',form_view,name='form'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)