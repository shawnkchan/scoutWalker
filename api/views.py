from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
import requests
from django.conf import settings
from django.http import JsonResponse

from .serializers import ShopSerializer
from .models import User, Shop, Reviews, ShopUpvote
# Create your views here.

### Class based view
class ShopView(APIView):
        
    def get(self, request):
        route = Shop.objects.all()
        serializers = ShopSerializer(route, many=True)
        # json = JSONRenderer().render(serializer.data)
        return Response({'status': 'success', "routes": serializers.data}, status=200)

    def post(self, request):
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        
        return Response({'status': 'error', 'data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

### Alternative: Function based view 
@api_view(['GET'])
def getShops(request):
    shop = Shop.objects.all()
    context = {
        'request': request
    }
    serializer = ShopSerializer(shop, many=True, context=context)
    return Response(serializer.data)
    
@api_view(['GET'])
def getShop(request, pk):
    shop = Shop.objects.get(id=pk)
    context = {
        'request': request
    }
    serializer = ShopSerializer(shop, many=False, context=context)
    return Response(serializer.data)

@api_view(['GET'])
def getKey(request):
    api_key = settings.API_KEY

    url = f"https://maps.googleapis.com/maps/api/js?key={api_key}&libraries=places"

    response = requests.get(url)
    return Response(response)

@api_view(['GET'])
def getLocations(request):
    