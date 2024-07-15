from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Enquiry(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=10,default=None)
    email=models.EmailField(max_length=30)
    subject=models.CharField(max_length=50)
    message=models.TextField()

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    forget_password_token=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

    