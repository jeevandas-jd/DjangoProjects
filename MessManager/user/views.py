from django.shortcuts import render
from .models import UserDetailes
import pywhatkit
def Admission(request):
    
    if request.POST:

        name=request.POST.get('name')
        dep=request.POST.get('dep')
        phone=request.POST.get('phone')
        year=request.POST.get('year')
        user_obj=UserDetailes(name=name,dep=dep,phone=phone,year=year)
        user_obj.save()
        pywhatkit.sendwhatmsg_instantly("+91"+phone,f"Dear {name} youre successfully admited to our mess\n your messID is{user_obj.pk},plase don't forget the IDnumber ,Thank you")
    return render(request,'admission.html')
def Home(request):
    return render(request,'home.html')
def profile(request):
    if request.POST:
        IDnumber=request.POST.get('IDnumber')
        info=UserDetailes.objects.get(pk=IDnumber)
        if info:
            return render(request,'show.html',{'info':info})
    else:
        return render(request,'profile.html')



#Create your views here.
