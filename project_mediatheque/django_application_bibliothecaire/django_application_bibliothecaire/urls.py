"""
URL configuration for django_application_bibliothecaire project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django_application_bibliothecaire import views

from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listeMembre),
    path('ajoutmembre/', views.ajoutmembre),
    path('updatemembre/<int:id>/', views.updatemembre),
    path('deletemembre/<int:id>/', views.deletemembre),
    path('ajoutlivre/', views.ajoutlivre),
    path('updatelivre/<int:id>/', views.updatelivre),
    path('deletelivre/<int:id>/', views.deletelivre),
    path('ajoutcd/', views.ajoutcd),
    path('updatecd/<int:id>/', views.updatecd),
    path('deletecd/<int:id>/', views.deletecd),
    path('ajoutdvd/', views.ajoutdvd),
    path('updatedvd/<int:id>/', views.updatedvd),
    path('deletedvd/<int:id>/', views.deletedvd),
    path('ajoutjdp/', views.ajoutjdp),
    path('updatejdp/<int:id>/', views.updatejdp),
    path('deletejdp/<int:id>/', views.deletejdp),






]

