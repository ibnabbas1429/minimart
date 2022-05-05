from django.urls import path,include

from .views import *


urlpatterns = [
    #path("register", register, "register"),
    path('' , login , name="login"),
    path('register' , register , name="register"),
    path('otp' , otp , name="otp"),
    path('login-otp', login_otp , name="login_otp")   
]