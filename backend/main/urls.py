from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from .models import *




urlpatterns = [
    path("", views.home, name = "home"),
    path("profile/<str:user>/", views.profile, name = "profile"),
    path("user/<str:username>/", views.profile_view, name = "profile_view"),
    path("profile_uploads/", views.profile_uploads, name = "profile_uploads"),
    path("profile_settings/<str:user>/", views.profile_settings, name = "profile_settings"),
    path("single_page/<str:id>/", views.single_page, name = "single_page"),
    path("delete_photo/<str:id>/", views.delete_photo, name = "delete_photo"),
    path("search/", views.profile_search_view, name = "search"),
    path("movie_list/", views.show_movie_list, name = "movie list"),
    path("upcoming_movie_list/", views.show_upcoming_movie_list, name = "upcoming movie list"),
    path('newmovie/<int:new_movie_id>/', views.new_movie_detail, name='new_movie_detail'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:movie_id>/write_review/', views.write_review, name='write_review'),
    path('movie/<int:movie_id>/book/', views.book_movie, name='book'),
    path('movie/payment/', views.payment, name='payment'),
    path('movie/payment/success', views.success, name='success'),
    path('hello_world', TemplateView.as_view(template_name='hello_world.html')),



]