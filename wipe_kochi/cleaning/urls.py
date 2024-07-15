"""
URL configuration for wipe_kochi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cleaning import views

urlpatterns = [
    path('cleaning/',views.service_view,name='cleaning'),
    path('detail_service/<int:pk>',views.detail_service,name='detail_service'),
    path('cleaning_booking/<int:pk>',views.cleaning_booking,name='cleaning_booking'),
    path('cleaning_success/',views.cleaning_success,name='cleaning_success'),




]
