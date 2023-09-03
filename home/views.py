from django.shortcuts import render
from .models import Health,Education,SOL,Governence,Culture
# Create your views here.
def home_view(request):
    return render(request,'home/homepage.html')

def asur_view(request):
    return render(request,'pvtg/asur.html')

def asur_view(request):
     health=Health.objects.all()
     education=Education.objects.all()
     sol=SOL.objects.all()
     culture=Culture.objects.all()
     governance=Governence.objects.all()
     health_incidence=0
     health_intensity=0
     education_incidence=0
     education_intensity=0
     sol_incidence=0
     sol_intensity=0
     culture_incidence=0
     culture_intensity=0
     governence_incidence=0
     governence_intensity=0
     for i in health:
        health_incidence+=i.H_incidence
        health_intensity+=i.H_intensity
     for i in education:
        education_incidence+=i.E_incidence
        education_intensity+=i.E_intensity
     for i in sol:
        sol_incidence+=i.S_incidence
        sol_intensity+=i.S_intensity
     for i in culture:
        culture_intensity+=i.C_incidence
        culture_incidence+=i.C_intensity
     for i in governance:
        governence_incidence+=i.G_incidence
        governence_intensity+=i.G_intensity

        # print(health_incidence)
        
        # print(health_intensity)
     health_index=health_incidence*health_intensity
     education_index=education_incidence*education_intensity
     sol_index=sol_incidence*sol_intensity
     culture_index=culture_incidence*culture_intensity
     governence_index=governence_incidence*governence_intensity
     
     context={
         'health':health,
         'education':education,
          "sol":sol,
          'culture':culture,
          'governance':governance,
          'health_index':health_index,
          'education_index':education_index,
          'sol_index':sol_index,
          'culture_index':culture_index,
          'governence_index':governence_index
          
           
     }
     return render(request,'pvtg/asur.html',context=context)
