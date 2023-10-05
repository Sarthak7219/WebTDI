from django.shortcuts import render
from .models import Household, Tribe
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    return render(request,'home/homepage.html')

def asur_view(request):
    tribe = Tribe.objects.get(id = 2)
    total_tribals = tribe.get_total_tribals()
    household = Household.objects.all()
    
    health_contributions_to_dimension=tribe.indicator_contributions_to_dimension()[0]
    education_contributions_to_dimension=tribe.indicator_contributions_to_dimension()[1]
    sol_contributions_to_dimension=tribe.indicator_contributions_to_dimension()[2]
    culture_contributions_to_dimension=tribe.indicator_contributions_to_dimension()[3]
    governance_contributions_to_dimension=tribe.indicator_contributions_to_dimension()[4]
    
    tribal_dimensional_index=tribe.tribal_dimensional_index()
    # tribal_index=tribe.tribal_index()
    dimension_contribution_to_tdi = tribe.dimension_contribution_to_tdi()
    
    context = {
        'household' : household,
        'total_tribals' : total_tribals,
        'tribe' : tribe,
        'health_contributions_to_dimension' : health_contributions_to_dimension,
        'education_contributions_to_dimension':education_contributions_to_dimension,
        'sol_contributions_to_dimension':sol_contributions_to_dimension,
        'culture_contributions_to_dimension':culture_contributions_to_dimension,
        'governance_contributions_to_dimension':governance_contributions_to_dimension,
        'tribal_dimensional_index' :tribal_dimensional_index,
        'dimension_contribution_to_tdi' :dimension_contribution_to_tdi
        
    }
    return render(request,'pvtg/asur.html',context=context)

# def asur_view(request):
     

#      health=Health.objects.all()
#      education=Education.objects.all()
#      sol=SOL.objects.all()
#      culture=Culture.objects.all()
#      governance=Governance.objects.all()
#      health_incidence=0
#      health_intensity=0
#      education_incidence=0
#      education_intensity=0
#      sol_incidence=0
#      sol_intensity=0
#      culture_incidence=0
#      culture_intensity=0
#      governance_incidence=0
#      governance_intensity=0
#      for i in health:
#         health_incidence+=i.H_incidence
#         health_intensity+=i.H_intensity
#      for i in education:
#         education_incidence+=i.E_incidence
#         education_intensity+=i.E_intensity
#      for i in sol:
#         sol_incidence+=i.S_incidence
#         sol_intensity+=i.S_intensity
#      for i in culture:
#         culture_intensity+=i.C_incidence
#         culture_incidence+=i.C_intensity
#      for i in governance:
#         governance_incidence+=i.G_incidence
#         governance_intensity+=i.G_intensity

#         # print(health_incidence)
        
#         # print(health_intensity)
      
#      health_index=round((health_incidence*health_intensity),2)
#      education_index=round((education_incidence*education_intensity),2)
#      sol_index=round((sol_incidence*sol_intensity),2)
#      culture_index=round((culture_incidence*culture_intensity),2)
#      governance_index=round((governance_incidence*governance_intensity),2)

#      HH_dimension_dev_score = health.score + education.score + sol.score  + culture.score  + governance.score
     
     
#      context={
#          'health':health,
#          'education':education,
#           "sol":sol,
#           'culture':culture,
#           'governance':governance,
#           'health_index':health_index,
#           'education_index':education_index,
#           'sol_index':sol_index,
#           'culture_index':culture_index,
#           'governance_index':governance_index
          
           
#      }
#      return render(request,'pvtg/asur.html',context=context)


def test_view(request):
    
    tribe = Tribe.objects.get(id = 2)
    total_tribals = tribe.get_total_tribals()
    household = Household.objects.all()
    
    
    
    context = {
        'household' : household,
        'total_tribals' : total_tribals,
        'tribe' : tribe,
        

    }
    return render(request, 'pvtg/test.html', context)

def form_view(request):
    if request.method == "POST":
        tribe = request.POST.get('tribe_name')
        size = request.POST.get('HH_size')
        HH_object = Household.objects.create(
            tribe_name = tribe,
            size = size,
            CD_score = request.POST.get('CD_score'),
            IM_score = request.POST.get('IM_score'),
            MC_score = request.POST.get('MC_score'),
            CM_score = request.POST.get('CM_score'),
            FS_score = request.POST.get('FS_score'),
            LE_score = request.POST.get('LE_score'),
            DRO_score = request.POST.get('DRO_score'),
            IC_score = request.POST.get('IC_score'),
            OW_score = request.POST.get('OW_score'),
            SANI_score = request.POST.get('SANI_score'),
            FUEL_score = request.POST.get('FUEL_score'),
            DRWA_score = request.POST.get('DRWA_score'),
            ELECTR_score = request.POST.get('ELECTR_score'),
            ASS_score = request.POST.get('ASS_score'),
            LAN_score = request.POST.get('LAN_score'),
            ARTS_score = request.POST.get('ARTS_score'),
            EV_score = request.POST.get('EV_score'),
            MEET_score = request.POST.get('MEET_score'),
        )
        HH_object.save()
        print('***************')
        return HttpResponse("Household added successfully!")


    return render(request, 'form/form.html')