from django.urls import path
from .views import *
name = "restfulapi"
urlpatterns = [
    path('', RestFulApiOverview, name ='home'),
    path('create/', add_commodity, name='add_commodity')
]
