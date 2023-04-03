from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.contrib import messages

import random
# Create your views here.
#img = Uploads.objects.all()

def home(request):
    return redirect(reverse("profile", args=[request.user]))




def profile(request, user):
    bookings = Booking.objects.filter(user=request.user)
    img = Uploads.objects.filter(profile_id=request.user.profile).order_by("-id")
    profile = Profile.objects.filter(user=request.user).first()
    context = {"profile": profile, "img": img, "bookings": bookings}
    return render(request, "main/profile.html", context)







def profile_view(request, username, *args, **kwargs,):
    context = {}
    try:
        user = User.objects.get(username=username)
        profile = user.profile
        img = profile.uploads_set.all().order_by("-id")

        context['username'] = user.username
    except:
        return HttpResponse("Something went wrong.")
    if profile:
        context = {"profile": profile, "img": img}

        return render(request, "main/profile_visit.html", context)




def profile_search_view(request, *args, **kwargs):
    context = {}
    if request.method == "GET":
        search_query = request.GET.get("q")
        if len(search_query) > 0:
            # Filter profiles
            profile_results = Profile.objects.filter(user__username__icontains=search_query).distinct()
            profiles = []
            for profile in profile_results:
                profiles.append((profile, False))  # you have no friends yet
            context['profiles'] = profiles
            
            # Filter movies
            movie_results = Movie.objects.filter(title__icontains=search_query)
            context['movies'] = movie_results

            new_movie_results = NewMovie.objects.filter(title__icontains=search_query)
            context['newmovies'] = new_movie_results
            
            # Filter theaters
            theater_results = Theater.objects.filter(name__icontains=search_query)
            context['theaters'] = theater_results

    return render(request, "main/search_results.html", context)




def profile_uploads(request):
    profile = request.user.profile
    if request.method == "POST":
        form = Uploads_Form(data = request.POST, files = request.FILES)
        if form.is_valid():
            form.instance.profile = request.user.profile
            form.save()
            obj = form.instance
            return redirect(reverse("profile", args=[request.user]))
    else:
        form = Uploads_Form()
    img = Uploads.objects.all()
    #profile = Profile.objects.filter(user = request.user).first()
    context = {"img":img, "form":form, "profile": profile}
    return render(request,"main/profile_uploads.html", context)




def profile_settings(request, user):
    profile = Profile.objects.filter(user = request.user).first()

    form = Profile_Form(instance = profile)
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES,instance = profile)
        if form.is_valid():
            form.save()
    context = {"profile": profile, "form": form}
    return render(request, 'main/profile_settings.html', context)


def single_page(request, id):
    img = Uploads.objects.filter(id = id).first()
    profile = Uploads.objects.filter(id = request.user.id)

    context = { "img": img, "profile": profile}

    return render(request, "main/single_page.html", context)


def delete_photo(request, id):
    if request.method == 'POST':
        img = Uploads.objects.get(id = id)
        img.delete()

    return redirect(reverse("profile", args=[request.user]))



def show_movie_list(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'main/movie_list.html', context)


def show_upcoming_movie_list(request):
    newmovies = NewMovie.objects.all()
    context = {'newmovies': newmovies}
    return render(request, 'main/upcoming_movie_list.html', context)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    context = {
        'movie': movie,'reviews': reviews
    }
    return render(request, 'main/movie_detail.html', context)

def new_movie_detail(request, new_movie_id):
    new_movie = get_object_or_404(NewMovie, pk=new_movie_id)
    context = {
        'new_movie': new_movie
    }
    return render(request, 'main/new_movie_detail.html', context)

def write_review(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'POST':
        review = Review.objects.create(
            profile=request.user.profile,
            movie=movie,
            review=request.POST['review']
        )
        return redirect('movie_detail', movie_id=movie_id)
    context = {'movie': movie}
    return render(request, 'main/write_review.html', context)


def book(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    context = {
        'movie': movie,'reviews': reviews
    }
    return render(request, 'main/book.html', context)




def book_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.movie = movie
            booking.save()
            request.session['booking_data'] = form.cleaned_data
            request.session['booking_id'] = booking.id
            return redirect('payment')
        else:
            print("error", form.errors)
    else:
        form = BookingForm()
    
    # Check if booking data is already saved in session
    if 'booking_data' in request.session:
        form = BookingForm(request.session['booking_data'])
    
    return render(request, 'main/book.html', {'movie': movie, 'form': form})



def payment(request):
    if request.method == 'POST':
        form = CreditCardForm(request.POST)
        if form.is_valid():
            # Save the credit card information
            credit_card = form.save(commit=False)
            credit_card.user = request.user
            credit_card.save()
            return render('success')
    else:
        form = CreditCardForm()
    return render(request, 'main/payment.html', {'form': form})

def success(request):
    random_number = random.randint(1, 100)
    context = {'random_number': random_number}
    return render(request, 'main/success.html', context)

