from django.shortcuts import render
from .models import About
# Create your views here.
def about(request):
    about = About.objects.last()
    template = 'about/about.html'
    context = {
        'about' : about
    }

    return render(request, template, context)