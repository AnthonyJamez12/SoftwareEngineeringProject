"""mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import *
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import *

admin.site.site_header = 'Proton Admin'
admin.site.site_title = 'Proton Admin'

from register.views import(
    register,
    logout,
    
)

from main.views import (
    home,
    profile,
    profile_view,
    profile_search_view,
    profile_uploads,
    profile_settings,
    single_page,
    delete_photo,
    make_account,
)

urlpatterns = [
    path('', include("main.urls")),
    path('', include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('register/', register, name = "register"),
    path('logout/', logout, name = "logout"),
    path('api/main/', include('main.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
