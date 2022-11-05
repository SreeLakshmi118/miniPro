from email.policy import default
from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Books(models.Model):
    b_name=models.CharField(max_length=250 ,unique=True)
    file=models.FileField(upload_to='pics')
    img=models.ImageField(upload_to='img')
    desc=models.TextField(blank=True)
    

    is_active=models.BooleanField(default=True)


    def __str__(self):
        return self.b_name

class Song(models.Model):
    s_name=models.CharField(max_length=250 ,unique=True)
    file=models.FileField(upload_to='song')
    img=models.ImageField(upload_to='imgs')
    desc=models.TextField(blank=True)
    

    is_active=models.BooleanField(default=True)


    def __str__(self):
        return self.s_name 
