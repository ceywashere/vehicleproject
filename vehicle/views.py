from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Vehicle
from .forms import VehicleForm


# Create your views here.
def vehicleHome(request):
    form = VehicleForm()
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Kayıt başarıyla eklendi")
            return redirect("vehicle:vehicle_home")
    context = {
        'form': form
    }

    return render(request, 'home.html', context)


def vehicleList(request):
    vehicles = Vehicle.objects.all()

    context = {
        'vehicles': vehicles
    }

    return render(request, 'vehicles.html', context)
