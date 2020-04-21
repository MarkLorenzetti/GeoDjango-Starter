from django import forms
from leaflet.forms.widgets import LeafletWidget

from leaflet.forms.fields import PointField
from .models import Event


class EventForm(forms.ModelForm):
	geom = PointField()

	class Meta:
		model = Event
		fields = ('name', 'geom')
		
	