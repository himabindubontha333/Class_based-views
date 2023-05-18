from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *
# Create your views here.

# FBV for returning string

def FBV_string(request):
    return HttpResponse('This is FBV string')

# CBV for returning string

class CBV_string(View):
    def get(self,request):
        return HttpResponse('This is CBV string')
    
# FBV for returning html page

def FBV_html(request):
    return render(request,'FBV_html.html')

# CBV for returning html page

class CBV_html(View):
    def get(self,request):
        return render(request,'CBV_html.html')

# FBV for returning forms

def FBV_form(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            return HttpResponse('Data is inserted')


    return render(request,'FBV_form.html',d)

# Handling forms by using CBV

class CBV_form(View):
    def get(self, request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'CBV_form.html',d)

    def post(self, request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')