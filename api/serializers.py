from dataclasses import field
import imp
from rest_framework import serializers
from bikes.models import Destination


class DestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'