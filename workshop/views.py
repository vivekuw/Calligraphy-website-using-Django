from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
# Create your views here.
def home(request):
    review =  Reviews.objects.all()
    return render(request,'index.html',{'review':review})

def about(request):
    return render(request,'about.html')

def course(request):
    Cou = Admission.objects.all()
    return render(request,'course.html',{'Cou':Cou})

def workshop(request):
    work = Workshop.objects.all()
    return render(request,'workshop.html' , {'work':work})

