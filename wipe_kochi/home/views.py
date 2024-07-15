from django.shortcuts import render,redirect
from.models import Enquiry,Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cleaning.models import Bookings
from scrap.models import Scrap_pickup


import uuid

from django.core.mail import send_mail
import uuid
from wipe_kochi import settings


# Create your views here.


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        phone=request.POST['phone']

        enq=Enquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message,
            )
        enq.save()

    return render(request,'contact.html')

def user_login(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST['username']
            password=request.POST['password']
            email=request.POST['email']
            # craete user account
            user=User.objects.create_user(username=username,password=password,email=email)

    
            success_message="user registered succesfully"
            messages.success(request,success_message)
        except Exception as e:
            error_message="The user name is alreday exist"
            messages.error(request,error_message)

    if request.POST and 'login' in request.POST:
        context['register']=False
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        if user and user.is_superuser == True:
            login(request,user)
            return admin_home(request)
        elif user:
            login(request,user)
            return home(request)
        else:
            messages.error(request,'invalid creadentials')

    return render(request,'login.html')


@login_required
def user_logout(request):
    logout(request)
    return home(request)

@login_required
def admin_home(request):
    return render(request,'admin_home.html')

@login_required
def service_details(request):
    booking=Bookings.objects.all()
    return render(request,'service_details.html',{'booking':booking})

@login_required
def scrap_details(request):
    pickup=Scrap_pickup.objects.all()
    return render(request,'scrap_details.html',{'pickup':pickup})



def change_password(request,token):
    context={}
    try:
        profile_obj=Profile.objects.filter(forget_password_token=token).first()
        context={'user_id':profile_obj.user.id}

        if request.method=='POST':
            new_password=request.POST.get('new_password')
            confirm_password=request.POST.get('confirm_password')
            user_id=request.POST.get('user_id')

            if user_id is None:
                messages.error(request,'No user id found')
                return redirect(f'/change_password/{token}')
            
            if new_password != confirm_password:
                messages.error(request,'*Password are not same')
                return redirect(f'/change_password/{token}')
            
            user_obj=User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect(user_login)
                

    except Exception as e:
        print(e)
    return render(request,'change_password.html',context)

def forget_password(request):
    try:
        if request.method=='POST':
            username=request.POST.get('username')

            if not User.objects.filter(username=username).first():
                messages.error(request,'Not user found with this username')
                return user_login(request)
            else:
            
                user_obj=User.objects.get(username=username)
                token=str(uuid.uuid4())
                
                Profile_obj=Profile.objects.create(user=user_obj)
                Profile_obj.forget_password_token=token
                Profile_obj.save()


                subject='Your forget password link'
                message=f'Hi, click on the link to rest your password http://127.0.0.1:8000/change_password/{token}'
                email_from=settings.EMAIL_HOST_USER
                recipient_list=[user_obj.email,]
                send_mail( subject,message,email_from,recipient_list)
                messages.success(request,'An email is send')

                return user_login(request)


    except Exception as e:
        print(e)

    return render(request,'forget_password.html')


