from django.urls import re_path,path, include
from .views import (
    home,
    lista_pessoas,
    pessoa_novo,
    lista_veiculos,
    veiculo_novo,
    lista_mov_rot,
    mov_rot_novo,
    lista_mov_mens,
    mov_mens_novo,
    lista_mensalistas,
    mensalista_novo,
    pessoa_update,
    veiculo_update,
    mov_rot_update,
    mensalista_update,
    mov_mens_update,
    pessoa_delete,
    mensalista_delete,
    veiculo_delete,
    mov_rot_delete,
    mov_mens_delete
)

urlpatterns = [
    path('', home, name='core_home'),
    re_path(r'^pessoas/$',lista_pessoas,name='core_lista_pessoas'),
    re_path(r'^pessoa-novo/$',pessoa_novo,name='core_pessoa_novo'),
    re_path(r'^pessoa-update/(?P<id>\d+)/$',pessoa_update,name='core_pessoa_update'),
    re_path(r'^pessoa-delete/(?P<id>\d+)/$',pessoa_delete,name='core_pessoa_delete'),

    re_path(r'^mensalistas/$',lista_mensalistas,name='core_lista_mensalistas'),
    re_path(r'^mensalista-novo/$',mensalista_novo,name='core_mensalista_novo'),
    re_path(r'^mensalista-update/(?P<id>\d+)/$',mensalista_update,name='core_mensalista_update'),
    re_path(r'^mensalista-delete/(?P<id>\d+)/$',mensalista_delete,name='core_mensalista_delete'),

    re_path(r'^veiculos/$',lista_veiculos,name='core_lista_veiculos'),
    re_path(r'^veiculo-novo/$',veiculo_novo,name='core_veiculo_novo'),
    re_path(r'^veiculo-update/(?P<id>\d+)/$',veiculo_update,name='core_veiculo_update'),
    re_path(r'^veiculo-delete/(?P<id>\d+)/$',veiculo_delete,name='core_veiculo_delete'),

    re_path(r'^mov-rot/$',lista_mov_rot,name='core_lista_mov_rot'),
    re_path(r'^mov-rot-novo/$',mov_rot_novo,name='core_mov_rot_novo'),
    re_path(r'^mov-rot-update/(?P<id>\d+)/$',mov_rot_update,name='core_mov_rot_update'),
    re_path(r'^mov-rot-delete/(?P<id>\d+)/$',mov_rot_delete,name='core_mov_rot_delete'),

    re_path(r'^mov-mens/$',lista_mov_mens,name='core_lista_mov_mens'),
    re_path(r'^mov-mens-novo/$',mov_mens_novo,name='core_mov_mens_novo'),
    re_path(r'^mov-mens-update/(?P<id>\d+)/$',mov_mens_update,name='core_mov_mens_update'),
    re_path(r'^mov-mens-delete/(?P<id>\d+)/$',mov_mens_delete,name='core_mov_mens_delete')

]
