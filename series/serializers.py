# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Serie


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff',
        'is_active', 'date_joined', 'last_login')


class SerieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Serie
        fields = ('id', 'name', 'release_date', 'rating', 'category')
