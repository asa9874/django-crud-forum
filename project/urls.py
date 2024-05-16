"""project URL Configuration

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
from django.urls import path,include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',views.index, name='index'),
    path('app/<int:voca_id>/', views.detail , name='detail'),
    path('answer/create/<int:voca_id>', views.answer_create , name='answer_create'),
    path('voca/create/', views.voca_create, name='voca_create'),
    path('voca/modify/<int:voca_id>/', views.voca_modify, name='voca_modify'),
    path('voca/delete/<int:voca_id>/', views.voca_delete, name='voca_delete'),
    path('voca/vote/<int:voca_id>/', views.voca_views.voca_vote, name='voca_vote'),

    
    path('common/',include('common.urls')),
    path('', views.index, name='index'),  # '/' 에 해당되는 path

]
