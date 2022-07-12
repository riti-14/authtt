from django.db import models


# Create your models here.

class empregister_model(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    confirm_password=models.CharField(max_length=20)

