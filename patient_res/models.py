from django.db import models

# Create your models here.
class User_Detail(models.Model):
    user_name =models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email= models.EmailField(max_length=254)
    phone_no= models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
	