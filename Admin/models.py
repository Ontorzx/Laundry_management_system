from django.db import models

# Create your models here.
class Customer(models.Model):
    C_id=models.CharField(blank=True,max_length=20)
    C_name=models.CharField(blank=True,max_length=50)
    C_email=models.EmailField(blank=False)
    C_address=models.TextField(max_length=100)
    C_contact=models.CharField(blank=True,max_length=20)
    delivary_date=models.DateTimeField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)