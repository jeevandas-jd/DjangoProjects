from django.db import models


class CensorInfo(models.Model):
    rating=models.CharField(max_length=10,null=True)
    authority=models.CharField(max_length=100,null=True)
# Create your models here.
class MovieInfo(models.Model):
    title=models.CharField(max_length=250)
    director=models.CharField(max_length=250)
    year=models.IntegerField(null=True)
    censor_info=models.OneToOneField(CensorInfo,on_delete=models.SET_NULL,related_name='movies')
    

