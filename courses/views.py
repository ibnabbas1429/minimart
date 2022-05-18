from django.shortcuts import render

# Create your views here.

from courses.models import Course
from courses.forms import CreateCourseForm



def course(request):
    pass

def creatCourse(request):

    form = CreateCourseForm(request.POST or None)

    if form.is_valid():

        form.save()

    context = {'form' : form}

    return render(request, "courses/register.html", context)
