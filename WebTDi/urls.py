from django.contrib import admin
from django.urls import path,include
from .views import home_view
from accounts.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view,name='home'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('register/',register_view, name='register'),
    path('tribe/', include('home.urls')),
    path('district/', include('district_wise.urls')),
]

