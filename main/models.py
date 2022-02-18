from django.db import models
from django.contrib.auth.models import User

from .validators import validate_is_audio

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = False, blank = True)
    first_name = models.CharField(max_length = 50, null = True, blank = True)
    last_name = models.CharField(max_length = 50, null = True, blank = True)
    phone = models.CharField(max_length = 50, null = True, blank = True)
    email = models.EmailField(max_length = 50, null = True, blank = True)
    bio = models.TextField(max_length = 300, null = True, blank = True)
    profile_picture = models.ImageField(default = 'default.png', upload_to = "img/%y", null = True, blank = True)
    banner_picture = models.ImageField(default = 'bg_image.png', upload_to = "img/%y", null = True, blank = True)

    def __str__(self):
        return f'{self.user.username} Profile'



class Uploads(models.Model):
    album = models.ForeignKey('Album', on_delete=models.SET_NULL,null=True,blank=True)    
    caption = models.CharField(max_length = 100, blank=True, null = True)
    file = models.ImageField(upload_to = "img/%y", null = True)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, default = None, null = True)
    id = models.AutoField(primary_key = True, null = False)


    def __str__(self):
        return str(self.file) and f"/single_page/{self.id}"

class Album(models.Model):
    name=models.CharField(max_length=400)
