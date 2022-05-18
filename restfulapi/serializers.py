"""creating a serializer using the ModelSerializer, 
an abstraction layer over the default that allows 
for quick creation of a serializer"""

from django.db .models import fields

from rest_framework import serializers

from .models Commodity


class ItemSerializer