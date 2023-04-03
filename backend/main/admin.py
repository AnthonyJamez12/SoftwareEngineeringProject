from django.contrib import admin
from .models import *

# Register your models here.

class UploadsInlineAdmin(admin.StackedInline):
    model = Uploads

class ProfileAdmin(admin.ModelAdmin):
    inlines = [UploadsInlineAdmin]
    

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Uploads)
admin.site.register(Movie)
admin.site.register(NewMovie)
admin.site.register(Theater)
admin.site.register(Review)
admin.site.register(Booking)
admin.site.register(CreditCard)