from rest_framework import serializers
from .models import Parking

class Parkingserializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        field = ['location', 'isParked']