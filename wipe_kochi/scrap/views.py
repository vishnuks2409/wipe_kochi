from django.shortcuts import render
from .models import Scrap_types,Scrap_pickup
from django.contrib.auth.decorators import login_required

@login_required
def Scrap(request):
    return render(request,'scrap.html')

@login_required
def scrap_type(request):
    type=Scrap_types.objects.all()
    return render(request,'scrap_type.html',{'types':type})

@login_required
def pickup(request,pk):
    cat=Scrap_types.objects.get(id=pk)

    
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        scrap_type=request.POST['category']
        email=request.POST['email']
        date=request.POST['date']
        address=request.POST['address']
        message=request.POST['remarks']

        u=request.user

        pickup=Scrap_pickup.objects.create(
            user=u,
            name=name,
            phone=phone,
            date=date,
            email=email,
            scrap_type=scrap_type,
            address=address,
            message=message
        )
        pickup.save()
        return success(request)
    return render(request,'scrap_pickup.html',{'cat':cat})

@login_required
def success(request):
    return render(request,'message.html')