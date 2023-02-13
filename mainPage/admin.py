from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import User, Route, RouteUpvote, RouteComment, FavouriteRoute

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')

class RouteAdmin(admin.ModelAdmin):
    list_display = ('distance', 'description', 'creator')

admin.site.register(User, UserAdmin)
admin.site.register(Route, RouteAdmin)