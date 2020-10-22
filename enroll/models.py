from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    Address=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    Delivery_date=models.DateField(null=True, blank=True)
