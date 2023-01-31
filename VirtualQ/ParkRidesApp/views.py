from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ParkRidesApp.models import ThemePark, ThemeParkArea, ThemeParkRide
from ParkRidesApp.serializers import (
    ThemeParkSerializer,
    ThemeParkAreaSerializer,
    ThemeParkRideSerializer
)

from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def parkAPI(request, id=0):
    # Get request method to retrieve all available parks
    if request.method == "GET":
        # Retrieve all the parks from the database
        theme_parks = ThemePark.objects.all()
        theme_parks_serializer = ThemeParkSerializer(theme_parks, many=True)
        # Return the serialized parks as a JSON response
        return JsonResponse(theme_parks_serializer.data, safe=False)
    # POST request method to add a park to the list.
    elif request.method == "POST":
        # Parse the incoming request data
        park_data = JSONParser().parse(request)
        # Serialize the data
        park_serializer = ThemeParkSerializer(data=park_data)
        # Validation for incoming data and save in the case of valid
        if park_serializer.is_valid():
            park_serializer.save()
            # Return a sucess message
            return JsonResponse("Park Added Successfully", safe=False)
        # Return a failure message if the incoming data is not valid
        return JsonResponse("Failed to add the park", safe=False)
    # PUT method to update a park in the list (Probably name in any case)
    elif request.method == "PUT":
        # Parse the incoming request data
        park_data = JSONParser().parse(request)
        # Retrieve the data, serialize it to update, however it is not compulsory to do
        park = ThemePark.objects.get(id=park_data["id"])
        park_serializer = ThemeParkSerializer(park, data=park_data)
        if park_serializer.is_valid():
            park_serializer.save()
            return JsonResponse("Park updated successfully", safe=False)
        return JsonResponse("Failed to update the park", safe=False)
    # DELETE method to remove the park
    elif request.method == "DELETE":
        park = ThemePark.objects.get(id=id)
        park.delete()
        return JsonResponse("Park deleted succesfully")

@csrf_exempt
def parkAreaAPI(request, id=0):
    #Get Request -> Get the list, serialize it and post it.
    if request.method == 'GET':
        parkareas = ThemeParkArea.objects.all()
        parkarea_serializer = ThemeParkAreaSerializer(parkareas, many=True)
        return JsonResponse(parkarea_serializer.data, safe=False)
    # POST request -> Post the request, serialize it, check if its valid and add it to the list if its good.
    elif request.method == 'POST':
        parkarea_data = JSONParser().parse(request)
        parkarea_serializer = ThemeParkAreaSerializer(data=parkarea_data)
        if parkarea_serializer.is_valid():
            parkarea_serializer.save()
            return JsonResponse("ThemeParkArea Added Successfully", safe=False)
        return JsonResponse("Failed to Add ThemeParkArea", safe=False)
    # PUT method request -> Updates the data from that one found on the request, serialize it and update in case that it's successful.
    elif request.method == 'PUT':
        parkarea_data = JSONParser().parse(request)
        parkarea = ThemeParkArea.objects.get(id=parkarea_data['id'])
        parkarea_serializer = ThemeParkAreaSerializer(parkarea, data=parkarea_data)
        if parkarea_serializer.is_valid():
            parkarea_serializer.save()
            return JsonResponse("ThemeParkArea Updated Successfully", safe=False)
        return JsonResponse("Failed to Update ThemeParkArea", safe=False)
    # DELETE method request -> Deletes the park area received. 
    elif request.method == 'DELETE':
        parkarea = ThemeParkArea.objects.get(id=id)
        parkarea.delete()
        return JsonResponse("ThemeParkArea Deleted Successfully", safe=False)

@csrf_exempt
def parkRidesAPI(request, id=0):
    # Get request to retrieve all park rides
    if request.method == "GET":
        park_rides = ThemeParkRide.objects.all()
        park_rides_serializer = ThemeParkRideSerializer(park_rides, many=True)
        return JsonResponse(park_rides_serializer.data, safe=False)

    # POST request to add a new park ride
    elif request.method == "POST":
        park_rides_data = JSONParser().parse(request)
        park_rides_serializer = ThemeParkRideSerializer(data=park_rides_data)
        if park_rides_serializer.is_valid():
            park_rides_serializer.save()
            return JsonResponse("Theme Park Ride added successfully!", safe=False)
        return JsonResponse("Failed to add a park ride", safe=False)

    # PUT request to update an existing park ride
    elif request.method == "PUT":
        park_rides_data = JSONParser().parse(request)
        park_ride = ThemeParkRide.objects.get(id=park_rides_data["id"])
        park_rides_serializer = ThemeParkRideSerializer(park_ride, data=park_rides_data)

        if park_rides_serializer.is_valid():
            park_rides_serializer.save()
            return JsonResponse("Park Ride has been updated successfully", safe=False)
        return JsonResponse("Failed to update park ride", safe=False)

    # DELETE request to delete a park ride
    elif request.method == "DELETE":
        park_ride = ThemeParkRide.objects.get(id=id)
        park_ride.delete()
        return JsonResponse("Park ride deleted successfully", safe=False)

@csrf_exempt
def saveFile(request):
    file = request.FILES["file"]
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
