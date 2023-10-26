from django.shortcuts import render
from .models import District
# Create your views here.
def district_view(request):
    district=District.objects.all()
    print(district)
    district_dimensional_index=district[0].get_dimension_scores()
    print(district_dimensional_index)
    Ddi=district[0].get_Ddi_score()
    print(Ddi)
    context={
      'district':district,
      'district_dimensional_index':district_dimensional_index,
      'Ddi':Ddi
    }
    return render(request, 'district/bokaro.html', context=context)

def test2_view(request):
    districts=District.objects.all()
    max_min_arr = districts.first().get_max_min_ind_scores()

    
    context={
        'districts':districts,
        'max_min_arr' : max_min_arr 
    }
    return render(request, 'district/test2.html', context=context)

