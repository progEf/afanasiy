from time import strftime

from django.db import models
from datetime import datetime

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    #created_at_1 = models.DateTimeField(auto_now_add=True, null=True, format='%Y-%m-%d')

class File_two(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class File_diskont(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
