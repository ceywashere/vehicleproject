from django.urls import path
from vehicle.views import vehicleList, vehicleHome

app_name = 'vehicle'

urlpatterns = [
    path('', vehicleHome, name='vehicle_home'),
    path('list/', vehicleList, name='vehicle_list'),


]
