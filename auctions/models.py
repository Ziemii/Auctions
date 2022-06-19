from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    pass
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # login = models.CharField(max_length=64, unique=True)
    # password = models.CharField(max_length=256)
    # email = models.EmailField()
    # def __str__(self):
    #     return f"{self.login}"


class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=25)
    description = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='userListings')
    bid = models.ForeignKey('Bid', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET('Other'), related_name='categoryListings')
    def __str__(self):
        return f"{self.title}"

class Bid(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # listing_id = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name='listingBids')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, related_name='userBids')
    def __str__(self):
        return f"{self.amount}"

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.TextField()
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, related_name='userComments')
    listing_id = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name='listingComments')
    datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.id}"

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.category}"
    