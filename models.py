from django.db import models
from django.contrib.gis.db import models as geomodels
from leaflet.forms.widgets import LeafletWidget



class Event(models.Model):
	name = models.CharField(max_length=100, blank=False)
	geometry = geomodels.PointField()
	
	
	class Meta:
		#order of drop-down list items
		ordering = ('name',)

        #plural form in admin view
		verbose_name_plural = 'events'
		
	@property
	def lat_lng(self):
		return list(getattr(self.geometry, 'coords', [])[::-1]) #PostGIS asks longitude and then latitude first while Leaflet is the opposite