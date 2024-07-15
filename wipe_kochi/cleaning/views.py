from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def service_view(request):
    service_obj=Cleaning.objects.all()
    return render(request,'service.html',{'service_obj':service_obj})
@login_required
def detail_service(request,pk):
    service=Cleaning.objects.get(id=pk)
    return render(request,'detail_service.html',{'service':service})
@login_required
def cleaning_booking(request,pk):
    obj=Cleaning.objects.get(id=pk)
   
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        service=request.POST['Service']
        email=request.POST['email']
        date=request.POST['date']
        address=request.POST['address']
        u=request.user

        bookings=Bookings.objects.create(
            user=u,
            name=name,
            phone=phone,
            date=date,
            email=email,
            service=service,
            address=address,
            
        )
        bookings.save()
        return cleaning_success(request)


    return render(request,'cleaning_booking.html',{'obj':obj})

@login_required
def cleaning_success(request):
    return render(request,'cleaning_message.html')