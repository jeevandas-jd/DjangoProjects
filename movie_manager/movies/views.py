from django.shortcuts import render
from .models import MovieInfo
from django.http import HttpResponse
from .forms import MovieForm
def Edit(request):
    movie_dataset=MovieInfo.objects.all()

    return render(request,"edit.html",{'movies':movie_dataset})
def Create(request):
    if request.POST:
        title=request.POST.get('title')
        director=request.POST.get('director')
        year=request.POST.get('year')
        movie_obj=MovieInfo(title=title,director=director,year=year)
        movie_obj.save()
        print(title,director,year)
    return render(request,'create.html')
def List(request):
    """movies_list={"movies":[{"title":"godha","year":2017,"director":"basil joseph","success":False,"image":'m2.png'},
                {"title":"kunjiramayanam","year":2015,"director":"basil joseph","success":True,"image":'m2.png'},
                {"title":"al Murali","year":2021,"director":"basil joseph","success":True,"image":'m2.png'},
                {"title":"ezra","year":2016,"director":"prithviraj","success":True,"image":'m2.png'},
                {"title":"Maraykar","year":2022,"director":"priyadaarshan","success":False,"image":'m2.png'},]}"""
    movie_dataset=MovieInfo.objects.all()
    return render(request,"list.html",{'movies':movie_dataset})
def Home(request):
    return render(request,'blank.html')
def delete(request,pk):
    instance=MovieInfo.objects.get(pk=pk)
    instance.delete()
    moive_set=MovieInfo.objects.all()
    return render( request,'edit.html',{'movies':moive_set})
def change(request,pk):
    instance_edit=MovieInfo.objects.get(pk=pk)
    if request.POST:
            title=request.POST.get('title')
            director=request.POST.get('director')
            year=request.POST.get('year')
            instance_edit.title=title
            instance_edit.year=year
            instance_edit.director=director
            instance_edit.save()
    frm=MovieForm(instance=instance_edit)
    return render(request,'change.html',{'instace_edit':instance_edit})


# Create your views here.
