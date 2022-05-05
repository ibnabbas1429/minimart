from django.contrib import admin

from .models import Course
from account.models import Profile

# Register your models here.

admin.site.register(Course)

#admin.site.register(Profile)