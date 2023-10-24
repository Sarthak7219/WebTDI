from django.urls import path
from .views import *

urlpatterns = [
  
    # path('<slug>/',name='tribe_detail'),
    path('test2/',test2_view,name='tribe_detail'),
   
]
