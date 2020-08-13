from django.contrib import admin
from .models import Staff
# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name' , 'age' ,'emp_id' , 'designation']
    list_filter = [ 'designation']
    search_fields = ['name' , 'age' ,'emp_id' , 'designation']
admin.site.register(Staff, StaffAdmin)