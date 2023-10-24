from django.shortcuts import render
from home.models import Tribe
# Create your views here.
def home_view(request):
    tribes = Tribe.objects.all()
    context = {
        'tribes' : tribes
    }
    return render(request,'home/homepage.html',context=context)

