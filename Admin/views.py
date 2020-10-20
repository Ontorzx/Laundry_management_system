from django.shortcuts import render
from .models import Customer
from .forms import CustomerDetails

# Create your views here.
def Home(request):
    context={

    }
    return render(request,'home.html',context)

def load_form(request):
    form=Customer
    context={
        'form':form,

    }
    return render(request,'index.html',context)

def add(request):
    form=Customer(request.POST)
    form.save()

def show (request):
    customer=Customer.objects.all
    context={
        'Customer':Customer,
    
    }
    return render (request,'show.html',context)

