'''The serializers define how the data from the models will be represented in the API. 
   Meta is used to specify the model and fields that the serializer should use'''

from rest_framework import serializers
from .models import ThemePark, ThemeParkArea, ThemeParkRide, Accessibility


class AccessibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessibility
        fields = ('id', 'wheelchair_access', 'audio_description', 'sign_language', 'braille', 'large_print')

class ThemeParkSerializer(serializers.ModelSerializer):
    """
    This class defines the serializer for the ThemePark model
    """
    class Meta:
        model = ThemePark
        fields = ('park_id', 'park_name')

class ThemeParkAreaSerializer(serializers.ModelSerializer):
    """
    This class defines the serializer for the ThemeParkArea model
    """
    class Meta:
        model = ThemeParkArea
        fields = ('area_id', 'area_name')

class ThemeParkRideSerializer(serializers.ModelSerializer):
    accessibility = AccessibilitySerializer()

    class Meta:
        model = ThemeParkRide
        fields = ('id', 'ride_name', 'ride_description', 'ride_thumbnail', 'ride_area', 'age_restriction', 'height_restriction', 'ride_type', 'ride_capacity', 'ride_duration', 'opening_hour', 'closing_hour', 'undermaintenance', 'park', 'accessibility')