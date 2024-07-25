from django.db import models

class UserDetailes(models.Model):
    name=models.TextField()
    dep=models.TextField()
    phone=models.CharField(max_length=15)
    year=models.IntegerField(null=True)
# Create your models here.
