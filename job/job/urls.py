from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from job import settings
from main.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('main.urls')),
]
