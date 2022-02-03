# -*- coding: utf-8 -*-

from urllib import request
from django.conf.urls import url
from django.urls import path


from apecsul.cadastro.views.views import igreja_view, igrejas_view
from . import views

app_name = 'cadastro'
urlpatterns = [
    # Cliente
    # cadastro/cliente/adicionar/
    url(r'cliente/adicionar/$',
        views.AdicionarClienteView.as_view(), name='addclienteview'),
    # cadastro/cliente/listaclientes
    url(r'cliente/listaclientes/$',
        views.ClientesListView.as_view(), name='listaclientesview'),
    # cadastro/cliente/editar/
    url(r'cliente/editar/(?P<pk>[0-9]+)/$',
        views.EditarClienteView.as_view(), name='editarclienteview'),

    # AJAX:: Informacoes de dada empresa (Ajax request)
    url(r'infocliente/$', views.InfoCliente.as_view(), name='infocliente'),
    url(r'selectcliente/', views.SelectFormCliente.as_view(), name='selectcliente'),
    path('igreja_view/<int:pk>', igreja_view, name='igreja_view'),
    path('igrejas_view/', igrejas_view, name='igrejas_view'),


]
