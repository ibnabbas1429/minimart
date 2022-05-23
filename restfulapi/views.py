from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status 
from .models import Commodity
from .serializers import CommoditySerializer

# Create your views here.

@api_view(['GET']) 
def RestFulApiOverview(request):
    api_urls ={
        'all_item': '/',
        'search by- category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)

    
#creating the CRUD Operations
#creating the create view to perform create operation

@api_view(['POST'])
def add_commodity(request):
    commodity = CommoditySerializer(data=request.data)
    #validating the already existing data
    if Commodity.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This Commodity already exist')

    if Commodity.is_valid():
        commodity.save()
        return Response(commodity.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


