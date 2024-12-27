from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import IntegerField, SlugField

class Categories(models.Model): 
    name = models.CharField(max_length=50, unique=True, verbose_name='Name') 
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta: 
        db_table = 'category' 
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Product')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name="Description")
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name="Image")
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Price")
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name="Discount in %")
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantity')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name="Category")
    
    
    class Meta: 
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = "Products"
        
    def __str__(self):
        return f'{self.name} Quantity: {self.quantity}'
    
    def display_id(self):
        return f'{self.id:05}'
    
    def sell_price(self): 
        if self.discount: 
            return round(self.price - self.price * self.discount/100, 2)
        return self.price