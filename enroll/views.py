from django.shortcuts import render,HttpResponseRedirect
from .forms import CustomerDetails
from enroll.models import User
# Create your views here.
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

        

    return render(request,'enroll/add_and_show.html',context)

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

def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

