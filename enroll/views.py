from django.shortcuts import render,HttpResponseRedirect
from .forms import CustomerDetails
from enroll.models import User
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

#Add the data through table

def add(request):
    if request.method == "POST":
        details=CustomerDetails(request.POST)
        if details.is_valid():
            details.save()
            details=CustomerDetails()
    else:
        details=CustomerDetails()
    show_details=User.objects.all()
    context={
        'details':details,
        'show_details':show_details,
    }

        
    
    return render(request,'enroll/add_customer.html',context)

#for show Customer Details

def add_show(request):
    if request.method == "POST":
        details=CustomerDetails(request.POST)
        if details.is_valid():
            details.save()
            details=CustomerDetails()
      

    else:
        details=CustomerDetails()
    show_details=User.objects.all()
    context={
        'details':details,
        'show_details':show_details,
    }

    
    return render(request,'enroll/customer_details.html',context)

#for Update operation of the Customer Details

def update_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        details=CustomerDetails(request.POST, instance=pi)
        if details.is_valid():
            details.save()
            return HttpResponseRedirect('/')
    else:
        pi=User.objects.get(pk=id)
        details=CustomerDetails(instance=pi)
   
    return render(request,'enroll/update.html',{'details':details})

#For delete operation of customer details

def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        messages.warning(request, 'Delete Customer Details Successfully.')
        return HttpResponseRedirect('/')

def search(request):
    if request.method=="POST":
        search_name=request.POST['name']
        pi=User.objects.filter(name__iexact=search_name)
        return render(request,'enroll/search_details.html',{'pi':pi}) 



