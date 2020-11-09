from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Product(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150,default='',blank=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=50,default='')
    featured = models.BooleanField(default=False)
    rating = models.FloatField(default=0,validators=[MaxValueValidator(5),MinValueValidator(0)])

    def __str__(self):
        return self.name

class Banner(models.Model):
    banner_name = models.CharField(max_length=50,default='')
    banner_image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.banner_name



class Offer(models.Model):
    offer_name = models.CharField(max_length=50,default='')
    offer_image = models.ImageField(upload_to='offer/')
    type = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.offer_name
