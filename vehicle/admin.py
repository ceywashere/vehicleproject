from django.contrib import admin
from .models import Vehicle


# Register your models here.


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'brand', 'plaka', 'driver', 'location']
    list_display_links = ('name',)

    class Meta:
        model = Vehicle
