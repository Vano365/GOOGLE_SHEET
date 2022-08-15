from django.urls import path, re_path
from django.views.decorators.cache import never_cache
from .views import *

urlpatterns = [
	path('', never_cache(IndexView.as_view()), name='index'),
]