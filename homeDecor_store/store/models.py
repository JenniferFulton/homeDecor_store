from django.db import models

class WarehouseManager(models.Manager):
    def newWarehouse_validator(self, postData):
        # validates a warehouse that is being added by a user
        errors = {}

        if len(postData['name']) <= 3:
            errors['name'] = 'Warehouse nickname must be atleast 3 characters'
        
        if postData['address'].isnumeric() == True or postData['address'].isalpha() == True:
            errors['address'] = 'Please include building number and street name in your address'
        
        if len(postData['city']) <= 2:
            errors['city'] = "Please include valid city"
        
        if len(postData['state']) != 2:
            errors['state'] = "Please use state abbreviation EX: MD for Maryland"
        
        if postData['zip_code'].isnumeric() == False or len(postData['zip_code']) != 5:
            errors['zip_code'] = 'Please use 5 numbers'
        
        return errors

class ItemManager(models.Manager):
    def newItem_validator(self, postData):
        # validates an item that is being added by a user
        errors = {}

        if len(postData['name']) <= 2:
            errors['name'] = 'Item name must be atleast 3 characters'
        
        if len(postData['description']) <= 5:
            errors['description'] = "Items's description must have more than 10 characters"
        
        if postData['height'].isnumeric() == True:
            errors['height'] = 'Please include number and units in your height dementions, Ex: 8" or 8 inches'
        
        if postData['width'].isnumeric() == True:
            errors['width'] = 'Please include number and units in your width dementions, Ex: 8" or 8 inches'
        
        if len(postData['color']) <= 2:
            errors['color'] = 'Color must be atleast 3 characters'
        
        if postData['quantity'].isnumeric() == False:
            errors['quantity'] = 'Please use numbers only for quantity'
        
        return errors

class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = WarehouseManager()

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
    objects = ItemManager()
