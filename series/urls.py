# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.contrib import admin
from series import views

urlpatterns = [
    url(r'^$', views.index, name='index'),    
    #####################
    ##### Using FBV #####
    #####################
    #url(r'^users/$', views.user_list),
    #url(r'^series/$', views.serie_list),
    #url(r'^series/(?P<pk>[0-9]+)/$', views.serie_detail),
    ######################################
    ##### Using CBV and CBV Generics #####
    ######################################
    url(r'^users/$', views.UsersList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^series/$', views.SeriesList.as_view()),
    url(r'^series/(?P<pk>[0-9]+)/$', views.SerieDetail.as_view()),
]