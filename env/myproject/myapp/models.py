from django.db import models

# Create your models here.
class Login(models.Model):

    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    def __str__(self):
        return self.username
class Register(models.Model):
    name=models.CharField(max_length=200)
    mail=models.CharField(max_length=250)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirmpassword=models.CharField(max_length=200,default=True)
    def __str__(self):
        return self.name
