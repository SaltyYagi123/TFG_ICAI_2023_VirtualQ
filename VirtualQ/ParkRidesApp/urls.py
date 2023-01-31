from django.urls import path
from . import views

urlpatterns = [
    path('parks/', views.parkAPI, name='park-list'),
    path('parks/<int:pk>/', views.parkAPI, name='park-detail'),
    path('rides/', views.parkRidesAPI, name='rides-list'),
    path('rides/<int:pk>/', views.parkRidesAPI, name='rides-detail'),
    path('rides/savefile', views.saveFile, name='parkride-img'),
    path('parkareas/', views.parkAreaAPI, name='parkarea-list'),
    path('parkareas/<int:id>/', views.parkAreaAPI, name='parkarea-detail')
]
