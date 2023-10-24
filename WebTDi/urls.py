from django.contrib import admin
from django.urls import path,include
from .views import home_view
from accounts.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view,name='home'),
    path('login/',login_view),
    path('logout/',logout_view),
    path('register/',register_view),
    path('tribe/', include('home.urls')),
    path('district/', include('district_wise.urls')),
]

