from django.contrib import admin
from .models import Restaurant
# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name' , 'location']
    search_fields = ['name' , 'location']
admin.site.register(Restaurant , RestaurantAdmin)