"""ripples URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from rippleswebsite import views as v1


urlpatterns = [
    path('adminpage/', admin.site.urls),
    path('', v1.mainpage),
    path('about/', v1.aboutus),
    path('events/', v1.events),
    path('signup/', v1.signup),
    path('signin/', v1.signin),
    path('te1/', v1.te1),
    path('te2/', v1.te2),
    path('te3/', v1.te3),
    path('nte1/', v1.nte1),
    path('nte2/', v1.nte2),
    path('nte3/', v1.nte3),
    path('logout/', v1.logout),
    path('mylist/', v1.mylist),


]
