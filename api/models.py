from enum import auto
from queue import Empty
from tkinter import CASCADE
from unicodedata import decimal
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    favourite_shop = models.ManyToManyField('Shop')
    #manytomany = item A can have many of item B, and vice versa

#store a shop's details
class Shop(models.Model):
    name = models.CharField(max_length=100, default='test')
    description = models.CharField(max_length=1000)
    tags = models.CharField(max_length=1000, null=True, blank=True)
    shop_image = models.ImageField(null=True, blank=True, upload_to='images/')
    website = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    average_rating = models.PositiveIntegerField(default=0)
    
    #should be able to add a shop to a list
 
#store the route's comments
class Reviews(models.Model):
    review = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_made')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE,related_name='reviews')

#store the route's upvotes
class ShopUpvote(models.Model):
    upvote = models.PositiveIntegerField(default=0)

class Locations(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    street = models.CharField(max_length=1000, null=True, blank=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='locations')
    

