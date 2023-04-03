from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from PIL import Image
from django.core.files import File
from django.core.validators import RegexValidator

class Profile_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "phone", "email", "bio", "profile_picture", "banner_picture")


class Uploads_Form(forms.ModelForm):
    album = forms.CharField(max_length=500,required=False)

    class Meta:
        model = Uploads
        fields = ("file", 'caption' )


class Reviews_Form(forms.ModelForm):
    review = forms.CharField(max_length=500,required=False)

    class Meta:
        model = Review
        fields = ("review",)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['tickets', 'seats', 'start_time', 'theater']
        labels = {
            'tickets': 'Number of Tickets',
            'seats': 'Number of Seats',
            'start_time': 'Start Time',
            'theater': 'Theatre Choices',
        },
        widgets = {
            'start_time': forms.RadioSelect(choices=Booking.start_time_choices),
            'theater': forms.RadioSelect(choices=Booking.theater_choices)
        }



class CreditCardForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ['name', 'card_number', 'card_expiry', 'card_cvv', ]