from django.db import models
from versatileimagefield.fields import VersatileImageField
from tinymce.models import HTMLField
from django.core.validators import MinValueValidator, MaxValueValidator


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
    
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    comment = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} for {self.product.name}"
