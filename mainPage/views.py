import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import User, Route
from django.conf import settings


json_serializer = serializers.get_serializer("json")()


# Create your views here.

def index(request):
    api_key = settings.API_KEY
    return render(request, 'mainPage/main.html', {
        'apiK': api_key
    })

def discover(request):
    routes = Route.objects
    routes = routes.order_by("-timestamp").all()
    return JsonResponse([route.serialize() for route in routes], safe=False)
