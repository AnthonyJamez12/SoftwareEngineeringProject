from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from decimal import Decimal

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = False, blank = True)
    first_name = models.CharField(max_length = 50, null = True, blank = True)
    last_name = models.CharField(max_length = 50, null = True, blank = True)
    address = models.CharField(max_length=100, null = True, blank = True)
    phone = models.CharField(max_length = 50, null = True, blank = True)
    email = models.EmailField(max_length = 50, null = True, blank = True)

    bio = models.TextField(max_length = 300, null = True, blank = True)
    profile_picture = models.ImageField(default = 'default.png', upload_to = "img/%y", null = True, blank = True)
    banner_picture = models.ImageField(default = 'bg_image.png', upload_to = "img/%y", null = True, blank = True)

    def __str__(self):
        return f'{self.user.username}'



class Uploads(models.Model):
    caption = models.CharField(max_length = 100, blank=True, null = True)
    file = models.FileField(upload_to = "img/%y", null = True)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE, default = None, null = True)
    id = models.AutoField(primary_key = True, null = False)


    def __str__(self):
        return str(self.file) and f"/single_page/{self.id}"








class Movie(models.Model):
    RATING_CHOICES = (
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC-17', 'Adults Only')
    )

    title = models.CharField(max_length=100, blank=True, null=True)
    synopsis = models.CharField(max_length=500, blank=True, null=True)
    hourTime = models.IntegerField()
    minuteTime = models.IntegerField()
    age_rating = models.CharField(max_length=5, choices=RATING_CHOICES, null=True)
    cast = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='movie_images/%y', blank=True, null=True)
    


    def __str__(self):
        return self.title

    
class NewMovie(models.Model):
    RATING_CHOICES = (
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC-17', 'Adults Only')
    )

    title = models.CharField(max_length=100, blank=True, null=True)
    synopsis = models.CharField(max_length=500, blank=True, null=True)
    hourTime = models.IntegerField()
    minuteTime = models.IntegerField()
    age_rating = models.CharField(max_length=5, choices=RATING_CHOICES, null=True)
    cast = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='movie_images/%y', blank=True, null=True)
    


    def __str__(self):
        return self.title



class Theater(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater_choices = [
        ('PREMIERE LUX Cine 10', 'PREMIERE LUX Cine 10'),
        ('Cinema 1 & 2', 'Cinema 1 & 2'),
        ('Cinemark Town Centre Cinema 6', 'Cinemark Town Centre Cinema 6'),
        ('Cinemark', 'Cinemark'),
        ('PREMIERE LUX 16 IMAX','PREMIERE LUX 16 IMAX')
    ]
    theater = models.CharField(max_length=50, choices=theater_choices, null = False, blank = False)
    start_time_choices = [
        ('10:00', '10:00 AM'),
        ('12:00', '12:00 PM'),
        ('15:00', '3:00 PM'),
        ('18:00', '6:00 PM')
    ]
    start_time = models.CharField(max_length=5, choices=start_time_choices, null = False, blank = False)
    tickets = models.IntegerField(default=1, null = False, blank = False, validators=[MaxValueValidator(10)])
    seats = models.IntegerField(default=1, null = False, blank = False, validators=[MaxValueValidator(10)])
    total_amount = models.DecimalField(
        max_digits=8, decimal_places=2,
        default=Decimal('0.00'), editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title} - {self.theater} - {self.start_time}'

    def save(self, *args, **kwargs):
        self.total_amount = Decimal('7.5') * self.tickets
        super().save(*args, **kwargs)



class CreditCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16, null = False, blank = False,)
    card_number = models.IntegerField(max_length=16, null = False, blank = False,)
    card_expiry = models.IntegerField(max_length=4,  null = False, blank = False,)
    card_cvv = models.IntegerField(max_length=3, null = False, blank = False,)


    def __str__(self):
        return f'{self.user.username} - {self.card_number}'

    