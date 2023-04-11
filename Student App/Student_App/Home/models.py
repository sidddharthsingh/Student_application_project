from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField(unique=True)
    Class=models.IntegerField()
    Age=models.IntegerField()
    City=models.CharField(max_length=20)
    