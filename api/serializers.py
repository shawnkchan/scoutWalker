
from urllib import request
from rest_framework import serializers 
from .models import User, Shop

class ShopSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField('get_photo_url')
    #meta class enables us to establish additional configuration options
    # allows you to specify various settings and metadata related to the serializer and the associated model.
    class Meta:
        #specifiying which model class that the serializer is referencing
        #this helps the serializer determine the fields and relationships to include.
        model = Shop
        #Only these specified fields will be serialized, and any other fields will be excluded.
        fields = ('id', 'name', 'description','tags','photo_url', 'website', 'instagram', 'average_rating' )

    def get_photo_url(self, Shop):
        request = self.context.get('request')
        photo_url = Shop.shop_image.url
        return request.build_absolute_uri(photo_url)
            

class UserSerializer(serializers.ModelSerializer):
    routes = ShopSerializer(many=True)

    class Meta: 
        model = User
        fields = ('id', 'username', 'routes')