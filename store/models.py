"""
A model representing a product in an online store.

Attributes:
    product_name (str): The name of the product.
    slug (str): A unique identifier for the product.
    description (str): A description of the product.
    price (int): The price of the product.
    stock (int): The current stock level of the product.
    is_available (bool): A boolean indicating whether the product is available for purchase.
    images (ImageField): A file upload field for product images.
    category (ForeignKey): A foreign key reference to the product's category.
    created_date (DateTimeField): The date the product was created.
    modified_date (DateTimeField): The date the product was last modified.

Methods:
    get_url(self): Returns the URL for the product's detail page.
    __str__(self): Returns the product's name.
"""

from django.db import models
from category.models import Category
from django.urls import reverse

class Product(models.Model):
    product_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=200, blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    images = models.ImageField(upload_to='photos/products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name




    

    