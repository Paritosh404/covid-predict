from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Data(models.Model):
    Name = models.CharField(max_length=50,unique=True)
    Q1 = models.CharField(max_length=50,default='false')
    Q2 = models.CharField(max_length=50,default='false')
    Q3 = models.CharField(max_length=50,default='false')
    Q4 = models.CharField(max_length=50,default='false')
    Q5 = models.CharField(max_length=50,default='false')
    Q6 = models.CharField(max_length=50,default='false')

    def __str__(self):
        return ' {0} '.format(self.Name)