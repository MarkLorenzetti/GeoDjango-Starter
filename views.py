# Create your views here.

from django.views.generic.list import ListView
from .models import Event

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import EventForm


class EventsListView(ListView):
    """
        Events to display on the map.
    """
    template_name = 'cities/map.html'
    model = Event
	
	
def FormView(request):
	if request.method == "POST":
		form = EventForm(request.POST)
		if form.is_valid():
			print("Il form è valido")
			#https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/#the-save-method
			data = form.save(commit=False)
			coordinates = request.POST['geom'] #The coordinates from the front-end have to be caught from the request first 
			data.geometry = coordinates
			data.save()
			print(data)		
			return HttpResponseRedirect("/events/")
	else:
		form = EventForm()
	context = {"form": form}
	return render(request, "cities/form.html", context)
	
	
