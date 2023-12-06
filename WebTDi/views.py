from django.shortcuts import render
from home.models import Tribe
from district_wise.models import District
# Create your views here.
def home_view(request):
    tribes = Tribe.objects.all()
    districts = District.objects.all()

    tribe_wise_tdi = []
    for tribe in tribes:
        tribe_wise_tdi.append(tribe.tribal_index)
    


    districts_name = []
    for district in districts:
        districts_name.append(district.name)


    district_wise_tdi = []
    for district in districts:
        district_wise_tdi.append(district.get_tdi_score()[0])

    context = {
        'tribes' : tribes,
        'tribe_wise_tdi' : tribe_wise_tdi,
        'districts_name' : districts_name,
        'district_wise_tdi' : district_wise_tdi
    }
    return render(request,'home/homepage.html',context=context)

