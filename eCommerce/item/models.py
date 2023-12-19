from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta():
        ordering = ['name',] # sort by alphabet
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='product', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    

