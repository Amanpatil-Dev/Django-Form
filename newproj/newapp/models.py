from django.db import models

# Create your models here.
class Form(models.Model):
    username=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    gender=models.CharField(max_length=5,default="")
    phoneno=models.IntegerField(default=0)
    desc=models.CharField(max_length=223,default="")



    def __str__(self):
        return self.username