from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path("", views.home, name = "home"),
    path("profile", views.profile, name = "profile"),
    path("profile_uploads", views.profile_uploads, name = "profile_uploads"),
    path("profile_settings", views.profile_settings, name = "profile_settings"),
    path('hello_world', TemplateView.as_view(template_name='hello_world.html'))

]
