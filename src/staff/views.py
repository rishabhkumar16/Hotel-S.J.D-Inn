from django.shortcuts import render
from .models import Staff
# Create your views here.
def staff_list(request):
    staff_list = Staff.objects.all()
    template = 'staff/staff.html'
    context = {
        'staff_list' : staff_list
    }

    return render(request, template, context)