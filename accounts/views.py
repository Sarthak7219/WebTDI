from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def register_view(request):
  form=UserCreationForm(request.POST or None)
  context={
  "form":form
  }
  if form.is_valid():
     obj=form.save()
 
  return render(request,'accounts/register.html',context)



def logout_view(request):
    context={}
    if request.method=="POST":
       logout(request)
       return render(request,"./accounts/login.html")
    return render(request,"accounts/logout.html",context)



def login_view(request):
  form=AuthenticationForm()
  context={}
  if request.method=='POST':
    form=AuthenticationForm(request,data=request.POST)
    if form.is_valid():
      user=form.get_user()
      login(request,user)
      return redirect("home/homepage.html")
  else:
      form=AuthenticationForm(request)
  context={
      "form":form
    }
  return render(request,"accounts/login.html",context)