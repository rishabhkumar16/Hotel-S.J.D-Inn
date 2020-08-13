from django.shortcuts import render
from property.models import Property  
from .models import Restaurant
# Create your views here.
def home(request):
    
    restaurant_list = Restaurant.objects.all()
    template = 'home/home.html'
    context = {
        'restaurant_list': restaurant_list
    }

    return render(request, template, context)