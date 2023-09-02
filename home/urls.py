from django.contrib import admin
from django.urls import path
from .views import home_view,asur_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view,name='hg'),
    path('asur/',asur_view,name='asur')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)