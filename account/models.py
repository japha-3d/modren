from django.db import models
from django.contrib.auth.models import  AbstractUser

class Custom(AbstractUser):
    age=models.PositiveIntegerField(null=True,blank=True)
    phone=models.CharField(max_length=11,unique=True)
    email=models.EmailField()

    

    