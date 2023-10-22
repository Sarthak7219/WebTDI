from django.shortcuts import render
from .models import District
# Create your views here.
def district_view(request):
    context={}
    return render(request, 'district/bokaro.html', context=context)

def test2_view(request):
    districts=District.objects.all()
    
    context={
        'districts':districts,
        
        
    }
    return render(request, 'district/test2.html', context=context)

