from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Scrap_types(models.Model):
    category=models.CharField(max_length=30)
    image=models.ImageField(upload_to='media/scrap',blank=True,null=True)

    def __str__(self):
        return self.category
    
class Scrap_pickup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    phone=models.BigIntegerField()
    scrap_type=models.CharField(max_length=30)
    date=models.DateField()
    email=models.CharField(max_length=30)
    address=models.TextField()
    message=models.TextField()

    def __str__(self):
        return self.name
    
    