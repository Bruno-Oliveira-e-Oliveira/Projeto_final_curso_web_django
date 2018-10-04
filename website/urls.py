from django.urls import path, include, re_path
from .views import home

urlpatterns = [
    re_path('^$',home,name='website_home'),
]