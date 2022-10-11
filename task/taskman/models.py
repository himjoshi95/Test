from unittest.util import _MAX_LENGTH
from venv import create
from django.db import models
from django.contrib.auth.models import User
import datetime 

# create your models here

class Task(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(max_length=200,null=True)
    complete = models.BooleanField(default=False)
    deadline = models.DateField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add = True)

    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']



    

