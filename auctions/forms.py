from .models import Listing, Bid, Comment
from django.forms import DecimalField, ModelForm, MultipleChoiceField, NumberInput, TextInput, Textarea, URLInput, Select

class CategorySelect(Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['category'] = value.instance.category
        return option

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'image_url', 'description', 'category', 'initial_bid']
        widgets = {
            'title' : TextInput(attrs={'class':'form-control'}),
            'image_url': URLInput(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'cols': 80, 'rows': 20, 'class':'form-control'}),
            'category': CategorySelect(attrs={'class': 'form-control'}),
            'initial_bid': NumberInput(attrs={'class': 'form-control w-25', 'placeholder': '0.00$'})
        }

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']