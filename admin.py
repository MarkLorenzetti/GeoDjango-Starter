from django.contrib import admin
from .models import Event
from leaflet.admin import LeafletGeoAdmin


class CityAdmin(LeafletGeoAdmin):
    # fields to show in admin listview
    list_display = ('name', 'geometry')


# register models in the admin site
admin.site.register(Event, CityAdmin)