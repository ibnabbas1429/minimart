from django.shortcuts import render
from django.contrib.auth.models import User

from .models import Profile

from .forms import ProfileForm


import random

# Create your views here.

def login(request):

    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {'form' : form}

    return render(request, "login.html", context)

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        
        check_user = User.objects.filter(email = email).first()
        check_profile = Profile.objects.filter(mobile = mobile).first()
        
        if check_user or check_profile:
            context = {'message' : 'User already exists' , 'class' : 'danger' }
            return render(request,'register.html' , context)
            
        user = User(email = email , first_name = name)
        print(user)
        user.save()
        otp = str(random.randint(1000 , 9999))
        profile = Profile(user = user , mobile=mobile , otp = otp) 
        profile.save()
        """send_otp(mobile, otp)
        request.session['mobile'] = mobile
        return redirect('otp')"""
    return render(request,'register.html')

    """if request.method == "POST":
        email = request.POST.get('email')
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        mobile = request.POST.get('mobile')
        
        check_user = User.objects.filter(email = email).first()

        check_profile = Profile.objects.filter(mobile = mobile).first()
        
        
        if check_user or check_profile:
            context = {'message' : "User already exist", "class": "danger"}
        
            return render(request, "register.html", context)

        user  = User(email= email, first_name=first_name)

        user.save()

        
        otp = str(random.randint(000000,999999))

        profile =Profile(user =user, mobile=mobile) 
        profile.save()
    return render(request, 'register.html',)"""

def otp(request):
    pass

def login_otp(request):
    pass
