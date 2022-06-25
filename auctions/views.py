from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ListingForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Bid, Category, Comment, Watchlist

@require_http_methods(["GET"])
def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        'Listings' : listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create(request):
    if request.method == "POST":
        f = ListingForm(request.POST)
        if f.is_valid():
            l = Listing(
                title=f.cleaned_data['title'],
                image_url=f.cleaned_data['image_url'],
                user=request.user,
                description=f.cleaned_data['description'],
                current_bid=f.cleaned_data['current_bid'],
                category=f.cleaned_data['category']
                )
            l.save()
            try:
               l = Listing.objects.get(title=f.cleaned_data['title'])
            except (Listing.DoesNotExist, Listing.MultipleObjectsReturned):
                return render(request, "auctions/error.html",{
                    "error" : "Error occured, please try again."
                })
        return redirect(f"/{l.id}")
    else: 
        return render(request, "auctions/create.html", {
            "listing_form" : ListingForm()
        })
    
@require_http_methods(["GET"])
def listing(request, id):
    listing = Listing.objects.get(pk = id)
    highestBid = None
    winning = False
    step = 0.01
    on_watchlist = False
    bids = Bid.objects.all().filter(listing_id = id)
    nOfBids =  Bid.objects.all().filter(listing_id = id).count()
    comments = Comment.objects.filter(listing_id = listing)
    if request.user.is_authenticated:
        on_watchlist = Watchlist.objects.filter(user = request.user, listing = listing)
    
    


    if(bids):
        highestBid = bids.order_by('-amount')[0]
        if(highestBid.user_id == request.user):
            winning = True
    
    return render(request, "auctions/listing.html",{
        'listing': listing,
        'nOfBids' : nOfBids,
        'highestBid' : highestBid,
        'winning':winning,
        'on_watchlist' : on_watchlist,
        'step' : step,
        'minimum' : float(listing.current_bid) + step,
        'comments' : comments,


    })

def user(request, id):
    return render(request, "auctions/user.html", {
        'Listings' : Listing.objects.all().filter(user = id),
        'username' : User.objects.get(pk = id)
    })
def category(request, category):
    return render(request, "auctions/category.html", {
        'Listings' : Listing.objects.all().filter(category = Category.objects.get(category = category)),
        'category' : category
    })

@login_required
@require_http_methods(["POST"])
def bid(request):
    user =  request.user
    bid_amount = request.POST['amount']
    listing = Listing.objects.get(id = request.POST['listing'])
    try:
        bid = Bid(listing_id = listing, user_id = user, amount = bid_amount)
        bid.save()
        listing.current_bid = bid_amount
        listing.save()
    except Exception:
        return render(request, "auctions/error.html", {
            'error' : "Error occured, please try again."
        })
    return redirect(f"/{listing.id}")


def categories(request):
    return render(request, "auctions/categories.html", {
        'categories' : Category.objects.all(),
    })

@login_required
@require_http_methods(["POST"])
def watchlist(request):
    try:
        user = User.objects.get(pk = request.user.id) 
        listing = Listing.objects.get(id = request.POST['listing'])
        try:
            watchlist = Watchlist.objects.get(user=user, listing=listing)
            if(watchlist):
                watchlist.delete()
        except Watchlist.DoesNotExist:
            watchlist = Watchlist(user=user, listing=listing)
            watchlist.save()
    except Exception:
        return render(request, "auctions/error.html", {
            'error' : "Error occured, please try again."
        })   
    return redirect(f"/{listing.id}")

@login_required
@require_http_methods(["POST"])
def comment(request):
    user =  User.objects.get(pk = request.user.id)
    comment = request.POST['comment']
    listing = Listing.objects.get(id = request.POST['listing'])

    try:
        new_comment = Comment(comment=comment, user_id=user, listing_id=listing)
        new_comment.save()
    except Exception:
        return render(request, "auctions/error.html", {
            'error' : "Error occured, please try again."
        })
    return redirect(f"/{listing.id}")

@login_required
@require_http_methods(["POST"])
def close(request):
    user =  User.objects.get(pk = request.user.id)
    listing = Listing.objects.get(id = request.POST['listing'])
    winner = Bid.objects.all().filter(listing_id = listing).order_by('-amount')[0].user_id
    #[FIXME:]
    print(f"winner: {winner}")