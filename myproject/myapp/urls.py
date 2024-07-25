from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.print_hello, name='print_hello'),
]
