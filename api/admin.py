from django.contrib import admin
from .models import User, Shop, Reviews, ShopUpvote, Locations

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')

class ShopAdmin(admin.ModelAdmin):
    list_display = ('id','description', 'name', 'description', 'tags', 'shop_image',)

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('review', 'user', 'shop')

class LocationsAdmin(admin.ModelAdmin):
    list_display = ('lat','lng','shop', 'street')

admin.site.register(User, UserAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Locations, LocationsAdmin)