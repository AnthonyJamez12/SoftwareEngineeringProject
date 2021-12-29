from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = "home"),
    path("profile", views.profile, name = "profile"),
    path("profile_uploads", views.profile_uploads, name = "profile_uploads"),
    path("profile_settings", views.profile_settings, name = "profile_settings"),

]
