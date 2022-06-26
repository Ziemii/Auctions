from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm
import uuid

# Django database models used in application 
# DB Engine: SQLite3

class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=25)
    image_url = models.URLField(blank=True, max_length=256)
    description = models.TextField()
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='userListings')
    current_bid = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.SET('Other'), related_name='categoryListings')
    winner = models.ForeignKey('User', on_delete=models.SET(None), null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.title}"

class User(AbstractUser):
    pass

class Bid(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing_id = models.ForeignKey('Listing', on_delete=models.CASCADE, related_name='listingBids')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, related_name='userBids')
    datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user_id}"

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

class Watchlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_watchlist')
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
    data = models.CharField(max_length=20)

    class Meta:
        unique_together = ('user', 'listing')

    def __str__(self):
        return f"{self.listing}"