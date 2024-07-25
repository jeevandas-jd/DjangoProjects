from django.urls import path

from . import views

urlpatterns =[
    path("",views.Home,name='Home'),
    path("Admission/",views.Admission,name='Admission'),
    path("Home/",views.Home,name='Home'),
    path("profile/",views.profile,name='profile')
]

