from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class ThemePark(models.Model):
    """
    This class defines the Theme Park model, it has an Park ID and a Park Name
    """
    park_id = models.CharField(max_length=10, primary_key=True, unique=True)
    park_name = models.CharField(max_length=255)
    
    def __str__(self):
        """
        This method is used to return a string representation of the object
        """
        return self.park_name

class ThemeParkArea(models.Model):
    """
    This class defines the Theme Park Area model, it has an Area ID and Area Name
    """
    area_id = models.CharField(max_length=10, primary_key=True, unique=True)
    area_name = models.CharField(max_length=255)
    park = models.ForeignKey(ThemePark, on_delete=models.CASCADE)
    
    def __str__(self):
        """
        This method is used to return a string representation of the object
        """
        return self.area_name

class Accessibility(models.Model):
    """
    Class representing the accessibility features of a theme park ride
    """
    wheelchair_access = models.BooleanField(default=False)
    audio_description = models.BooleanField(default=False)
    braille = models.BooleanField(default=False)
    sign_language = models.BooleanField(default=False)
    closed_captioning = models.BooleanField(default=False)
    tactile_path = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.id}'

class ThemeParkRide(models.Model):
    """
    This class defines the Theme Park Ride model, it has Ride ID, Ride Name, Ride Description, 
    Ride Thumbnail, Ride Area (Associated to the theme park area), Park (Associated to the theme park),
    Age Restriction, Height Restriction, Ride Type, Ride Capacity, Ride duration, 
    opening hour, closing hour,undermaintenance 
    """
    ride_id = models.CharField(max_length=10, primary_key=True, unique=True)
    ride_name = models.CharField(max_length=255)
    ride_description = models.TextField()
    ride_thumbnail = models.ImageField(upload_to='rides_images/')
    ride_area = models.ForeignKey(ThemeParkArea, on_delete=models.CASCADE)
    park = models.ForeignKey(ThemePark, on_delete=models.CASCADE)
    age_restriction = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    height_restriction = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(300)])
    ride_type = models.CharField(max_length=255)
    ride_capacity = models.PositiveIntegerField()
    ride_duration = models.DurationField()
    opening_hour = models.TimeField()
    closing_hour = models.TimeField(default='22:00:00')
    under_maintenance = models.BooleanField(default=False)
    accesibility = models.ForeignKey(Accessibility, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """
        This method is used to return a string representation of the object
        """
        return self.ride_name
    
    def park_open_hours(self):
        """
        This method returns the hours the park is open
        """
        return self.closing_hour - self.opening_hour
    
    def count_rides(self):
        """
        This method returns the number of rides in the park
        """
        return ThemeParkRide.objects.filter(park=self.park).count()

