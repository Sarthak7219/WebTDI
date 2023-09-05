from django.shortcuts import render
from .models import Household, Tribe
# Create your views here.
def home_view(request):
    return render(request,'home/homepage.html')

# def asur_view(request):
#     return render(request,'pvtg/asur.html')

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
    
    tribe = Tribe.objects.get(id = 1)
    total_tribals = tribe.get_total_tribals()
    household = Household.objects.all()

    context = {
        'household' : household,
        'total_tribals' : total_tribals,
        'tribe' : tribe
    }
    return render(request, 'pvtg/test.html', context)