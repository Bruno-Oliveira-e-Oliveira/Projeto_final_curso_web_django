from django.urls import path, include, re_path
from .views import home,contato,servicos,plano,sobre

urlpatterns = [
    re_path('^$',home,name='website_home'),
    re_path('^contato',contato,name='website_contato'),
    re_path('^servicos',servicos,name='website_servicos'),
    re_path('^sobre',sobre,name='website_sobre'),
    re_path('^plano',plano,name='website_plano'),
]