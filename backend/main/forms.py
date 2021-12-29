from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
from PIL import Image
from django.core.files import File

class Profile_Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "phone", "email", "bio", "profile_picture")


class Uploads_Form(forms.ModelForm):

    class Meta:
        model = Uploads
        fields = ("file",)
