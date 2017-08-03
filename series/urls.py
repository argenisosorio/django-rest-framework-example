# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.contrib import admin
from series import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.serie_list),
    #url(r'^series/$', views.serie_list),
]
