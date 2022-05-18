from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    height = models.CharField(max_length=30)
    width = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    quantity = models.CharField(max_length=100)
    image = models.ImageField(null=True)
    location = models.ManyToManyField(Warehouse,related_name="warehouse")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
