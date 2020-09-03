from django.shortcuts import render, redirect
from .models import Property,Category, Reserve
from .forms import ReserveForm

# Create your views here.
def property_list(request):
    property_list = Property.objects.all()
    template = 'property/list.html'
    context = {
        'property_list' : property_list
    }

    return render(request, template, context)

def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    template = 'property/detail.html'
    
    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid() :
            reserve_form.save()
    else :
        reserve_form = ReserveForm()
    # if request.method=='POST':
    #     r_no=request.POST.get('r_no')
    #     name=request.POST.get('name')
    #     email=request.POST.get('email')
    #     phone_number=request.POST.get('phone_no')
    #     no_of_children=request.POST.get('no_of_children')
    #     no_of_adult=request.POST.get('no_of_adult')
    #     check_in=request.POST.get('check_in')
    #     check_out=request.POST.get('check_out')
    #     name=Reserve(r_no=r_no, name=name, email=email, phone_number=phone_number, no_of_children=no_of_children, no_of_adult=no_of_adult, check_in=check_in,check_out=check_out)
    #     name.save()
    context = {
        'property_detail' : property_detail,
        'reserve_form' : reserve_form
    }
    return render(request, template, context)
