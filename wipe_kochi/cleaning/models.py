from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cleaning(models.Model):
    name=models.CharField(max_length=30)
    desc=models.TextField()
    image=models.ImageField(upload_to='media/image',blank=True,null=True)
    icon=models.ImageField(upload_to='media/icon',blank=True,null=True)
    title1=models.CharField(max_length=50)
    title2=models.CharField(max_length=50)
    title3=models.CharField(max_length=50)


    def __str__(self):
        return self.name
    

    
class Bookings(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    phone=models.BigIntegerField()
    service=models.CharField(max_length=30)
    date=models.DateField()
    email=models.CharField(max_length=30)
    address=models.TextField()


    def __str__(self):
        return self.name
    


