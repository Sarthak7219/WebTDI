from django.shortcuts import render
from .models import District
# Create your views here.
def district_view(request):
    district=District.objects.all()
    district_dimensional_index=district[0].get_dimension_scores()
    Ddi=district[0].get_tdi_score()
    health_ind_contri_to_dim=district[0].get_indicator_contri_to_dimension()[0]
    education_ind_contri_to_dim=district[0].get_indicator_contri_to_dimension()[1]
    sol_ind_contri_to_dim=district[0].get_indicator_contri_to_dimension()[2]
    normalized_final_ind_scores=district[0].get_normalized_final_ind_scores()
    health_contri_to_tdi=district[0].get_dimension_contribution_tdi()[0]
    education_contri_to_tdi=district[0].get_dimension_contribution_tdi()[1]
    sol_contri_to_tdi=district[0].get_dimension_contribution_tdi()[2]
    print(normalized_final_ind_scores)
    context={
      'district':district,
      'district_dimensional_index':district_dimensional_index,
      'Ddi':Ddi,
      'health_ind_contri_to_dim':health_ind_contri_to_dim,
      'education_ind_contri_to_dim':education_ind_contri_to_dim,
      'sol_ind_contri_to_dim':sol_ind_contri_to_dim,
      'normalized_final_ind_scores':normalized_final_ind_scores,
      'health_contri_to_tdi':health_contri_to_tdi,
      'education_contri_to_tdi':education_contri_to_tdi,
      'sol_contri_to_tdi':sol_contri_to_tdi

       

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

