from django.db import models
from versatileimagefield.fields import VersatileImageField
from tinymce.models import HTMLField

# Create your models here.

class Category(models.Model):
    image=VersatileImageField(upload_to='product_images/')
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    cover_image=VersatileImageField(upload_to='product_images/')
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = HTMLField()
    
    def __str__(self):
        return self.name


class Product_images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = VersatileImageField(upload_to='product_images/')