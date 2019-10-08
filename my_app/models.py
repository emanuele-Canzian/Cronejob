from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class CroneJob(models.Model):
    title = models.CharField(max_length=30, null='false', default='')
    url = models.CharField(max_length=30, null='false', default='')
    authentication = models.BooleanField(default='false')
    username = models.CharField(max_length=30, null='false', default='')
    password = models.CharField(max_length=100, null='false', default='')

