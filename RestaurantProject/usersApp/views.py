from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view, renderer_classes
from workersApp.models import MenuItems
from .serializers import MenuItemSerializer
from rest_framework.response import Response

# Create your views here

@api_view(['GET'])
@renderer_classes([TemplateHTMLRenderer])
def menu(request):
    items = MenuItems.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response({'data':serialized_item.data}, template_name='menu-items.html')
    

def home(request):
    return HttpResponse("Welcome to Home")




