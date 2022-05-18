from django import forms
from django.contrib.auth.models import User
from .models  import Course

class CreateCourseForm (forms.ModelForm):
        class Meta:
            course= Course.objects.all()
            '''first_name = user.first_name
            surname = user.lastname'''
            model =  Course
            
            fields = [
                'title',
                'author',
                


            ]