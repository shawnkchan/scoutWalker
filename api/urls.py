from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ShopView.as_view(), name='routes'),
    path('shops', views.getShops, name='shops'),
    path('shops/<str:pk>', views.getShop, name='singleShop'),
    path('key', views.getKey, name='key')
]