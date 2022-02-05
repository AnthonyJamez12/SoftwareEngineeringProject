from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from .models import *

urlpatterns = [
    path("", views.home, name = "home"),
    path("profile/<str:user>/", views.profile, name = "profile"),
    path("profile_uploads", views.profile_uploads, name = "profile_uploads"),
    path("profile_settings/<str:user>/", views.profile_settings, name = "profile_settings"),
    path("<str:user>/single_page/<int:id>", views.single_page, name = "single_page"),
    path('hello_world', TemplateView.as_view(template_name='hello_world.html')),

]
