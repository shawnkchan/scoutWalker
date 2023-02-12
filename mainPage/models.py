from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

#store the user's custom routes
class Route(models.Model):
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=1000)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='routes', null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    #should be able to favourite a route, manytomany rs
    #counter to record how many times the user has used it?
    #enable public access to the route
    def serialize(self):
        return {
            'id': self.id,
            'creator': self.creator.routes,
            'distance': self.distance,
            'description': self.description,
            'timestamp': self.timestamp
        }

#store the route's comments
class RouteComment(models.Model):
    pass

#store the route's upvotes
class RouteUpvote(models.Model):
    pass

#store the user's favourite routes
class FavouriteRoute(models.Model):
    pass