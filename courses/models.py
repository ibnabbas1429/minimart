from django.db import models

from minimart.settings import TIME_ZONE

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length= 300)
    author = models.CharField(max_length = 300)
    published = models.DateTimeField(default = TIME_ZONE)
    
    Created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Course {self.title} created by {self.author}  was on "
        