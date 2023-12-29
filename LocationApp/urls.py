from django.urls import path

from LocationApp import views

urlpatterns = [
    path('',views.LocationAPI.as_view()), # GET request : http://localhost:8000/location/

]