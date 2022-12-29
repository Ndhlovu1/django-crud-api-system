from django.shortcuts import render

# Imports for using the Serializers
from rest_framework import generics #Generics allow you to use the DRF automatic get and put and del/patch
from .models import MenuItems
from .serializers import MenuItemSerializer

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer

#The class below allows for Updating and Deleting through our API
class SingleItemView(generics.RetrieveUpdateDestroyAPIView, generics.UpdateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer





