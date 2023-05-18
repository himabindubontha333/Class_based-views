"""project38 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('FBV_string/',FBV_string,name='FBV_string'),
    path('CBV_string/',CBV_string.as_view(),name='CBV_string'),

    path('FBV_html/',FBV_html,name='FBV_html'),
    path('CBV_html/',CBV_html.as_view(),name='CBV_html'),

    path('FBV_form/',FBV_form,name='FBV_form.html'),
    path('CBV_form/',CBV_form.as_view(),name='CBV_form'),

    path('CBV_direct/',TemplateView.as_view(template_name='CBV_direct.html'),name='CBV_direct'),
]
