from django.contrib import admin

# Register your models here.
from .models import Property , Category , Reserve
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name','room_no' , 'type' ,'price' , 'no_of_beds']
    search_fields = ['name','type', 'room_no']
    list_filter = ['type', 'price', 'no_of_beds' ,'area']
class ReserveAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email', 'phone_number']
    search_fields = ['name' , 'email', 'phone_number']
admin.site.register(Property, PropertyAdmin)
admin.site.register(Reserve, ReserveAdmin)
admin.site.register(Category)

