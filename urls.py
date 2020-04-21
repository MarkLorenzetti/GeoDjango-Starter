from .views import EventsListView, FormView
from django.urls import path





urlpatterns = [
    path('', EventsListView.as_view(), name="map"),
    path('form/', FormView, name="form"),
]