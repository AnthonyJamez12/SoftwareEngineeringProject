from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from .models import *

from .views import (
    home,
    profile,
    profile_view,
    profile_search_view,
    profile_uploads,
    profile_settings,
    single_page,
    delete_photo,
    make_account,
    post_display_all_view,
    post_detail_view,
    
    
)



urlpatterns = [
    path("", home, name = "home"),
    path("profile/<str:user>/", profile, name = "profile"),
    #path("profile/", profile, name = "profile"),#################################
    path("make_account", make_account, name = "make_account"),
    path("user/<str:username>/", profile_view, name = "profile_view"),
    path("profile_uploads/", profile_uploads, name = "profile_uploads"),
    path("profile_settings/<str:user>/", profile_settings, name = "profile_settings"),
    path("single_page/<str:id>/", single_page, name = "single_page"),
    #path("single_page_visit/<str:id>/", single_page_visit, name = "single_page_visit"),
    path("delete_photo/<str:id>/", delete_photo, name = "delete_photo"),
    path("search/", profile_search_view, name = "search"),


    path('', post_display_all_view),
    path('<int:post_id>', post_detail_view),
    
    


]
