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


def index(request):
    """
    Index view, to tray.
    """
    return HttpResponse("Hello, world!")


##### Using CBV Generics ####
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

##### Using CBV ####
'''
class UsersList(APIView):
    """
    List all Users
    """
    def get(self, request, format=None):
        usuarios = User.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UserSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UserSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SeriesList(APIView):
    """
    List all Series
    """
    def get(self, request, format=None):
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        return Response(serializer.data)


class SerieDetail(APIView):
    """
    Retrieve, update or delete a serie instance.
    """
    def get_object(self, pk):
        try:
            return Serie.objects.get(pk=pk)
        except Serie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serie = self.get_object(pk)
        serializer = SerieSerializer(serie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        serie = self.get_object(pk)
        serializer = SerieSerializer(serie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        serie = self.get_object(pk)
        serie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

##### Using FBV ####
'''
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def user_list(request):
    """
    List all users.
    """
    if request.method == 'GET':
        usuarios = User.objects.all()
        serializer = UserSerializer(usuarios, many=True)
        return JSONResponse(serializer.data)


@csrf_exempt
def serie_list(request):
    """
    List all code serie.
    """
    if request.method == 'GET':
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SerieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def serie_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        serie = Serie.objects.get(pk=pk)
    except Serie.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SerieSerializer(serie)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SerieSerializer(serie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        serie.delete()
        return HttpResponse(status=204)
'''
