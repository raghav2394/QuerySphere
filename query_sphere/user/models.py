from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)



class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=True) 
    admin = models.BooleanField(default=False) 
   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Query(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    query = models.CharField(max_length=2000,help_text='Write here your query!')
