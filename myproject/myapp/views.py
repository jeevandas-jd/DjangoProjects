from django.http import HttpResponse
from django.shortcuts import render
def print_hello(request):
    movies_list={"movies":[{"title":"godha","year":2017,"director":"basil joseph","success":False},
                {"title":"kunjiramayanam","year":2015,"director":"basil joseph","success":True},
                {"title":"Minnal Mrali","year":2021,"director":"basil joseph","success":True},
                {"title":"ezra","year":2016,"director":"prithviraj","success":True},
                {"title":"Maraykar","year":2022,"director":"priyadaarshan","success":False},]}
    
    return render(request,"myapp/hello.html",movies_list)
