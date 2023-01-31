from django.contrib import admin
from .models import ThemePark, ThemeParkArea, ThemeParkRide

# Register the ThemePark model
admin.site.register(ThemePark)

# Register the ThemeParkArea model
admin.site.register(ThemeParkArea)

# Register the ThemeParkRide model
admin.site.register(ThemeParkRide)
