# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from series.models import Serie
from series.serializers import SerieSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from series.permissions import IsOwnerOrReadOnly


def index(request):
    return HttpResponse("Hello, world!")


class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SeriesList(generics.ListCreateAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer


class SerieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
