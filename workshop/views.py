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

def login(request):
    def user_login(request):
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']

            # Get user by email
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
            except User.DoesNotExist:
                user = None

            if user is not None:
                login(request, user)
                return redirect('/home')  # Redirect to profile or dashboard
            else:
                msg = 'Invalid email or password'
                form = AuthenticationForm(request.POST)
                return render(request, 'login.html', {'form': form, 'msg': msg})
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form } )


def register(request):
    return render(request,'login.html')