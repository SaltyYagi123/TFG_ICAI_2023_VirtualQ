from rest_framework import serializers
from .models import ThemePark, ThemeParkArea, ThemeParkRide

class ThemeParkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemePark
        fields = '__all__'

class ThemeParkAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeParkArea
        fields = '__all__'

class ThemeParkRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeParkRide
        fields = '__all__'
