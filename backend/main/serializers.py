from django.conf import settings
from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = False, blank = True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()
    bio = serializers.CharField()
    profile_picture = serializers.ImageField()
    banner_picture = serializers.ImageField()
    id = serializers.IntegerField()

    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "phone", "email", "bio", "profile_picture", "banner_picture", "id")

    def __str__(self):
        return f'{self.user.username}'




class UploadsSerializer(serializers.ModelSerializer):
    caption = serializers.CharField()
    file = serializers.ImageField()
    id = serializers.IntegerField(read_only = True)


    class Meta:
        model = Uploads
        fields = ("caption", "file", "id")


    def __str__(self):
        return str(self.file) and f"/single_page/{self.id}"
