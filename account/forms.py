from django import forms
from django.contrib.auth.models import User
from .models  import Profile

class ProfileForm (forms.ModelForm):
        class Meta:
            user= User.objects.all()
            '''first_name = user.first_name
            surname = user.lastname'''
            model =  Profile
            
            fields = [
                'user',
                'mobile',
                'otp'

            ]