# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.contrib import admin
from app import views

urlpatterns = [
	url(r'^', views.TestView.as_view(), name='test-view'),
]