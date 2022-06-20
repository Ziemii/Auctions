from .models import Listing, Bid, Comment
from django.forms import ModelForm, Textarea

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'image_url', 'description', 'category', 'initial_bid']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']