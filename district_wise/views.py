from django.shortcuts import render
from .models import District
# Create your views here.
def district_view(request):
    context={}
    return render(request, 'district/test2.html', context=context)

def test2_view(request):
    districts=District.objects.all()
    max_min_arr = districts.first().get_max_min_ind_scores()

    
    context={
        'districts':districts,
        'max_min_arr' : max_min_arr 
    }
    return render(request, 'district/test2.html', context=context)

