from dataclasses import field
from rest_framework import serializers


from .models import *




class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = "__all__"