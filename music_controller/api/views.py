from django.shortcuts import render
from django .http import HttpResponse
from rest_framework import generics
from .models import Room
from . serializer import Roomserializer


# Create your views here.
def main(request):
    return HttpResponse('hello')

class RoomView(generics.CreateAPIView):
    queryset=Room.objects.all()
    serializer_class=Roomserializer

class ListView(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=Roomserializer