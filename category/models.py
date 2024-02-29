from django.db import models
from django.urls import reverse 

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length= 100, unique = True)
    slug = models.SlugField(max_length=150, unique = True)
    descrption = models.TextField(max_length=250, blank = True)
    image =models.ImageField(upload_to='photos/categories', blank =True)


    def get_url(self):
        return reverse('product_by_category', args = [self.slug])


    def __str__(self):
        return self.category_name
