# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.contrib import admin
from series import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', views.user_detail),
    url(r'^series/$', views.serie_list),
    url(r'^series/(?P<pk>[0-9]+)/$', views.serie_detail),
]
