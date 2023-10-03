from django.urls import path

from HotelApp import views

urlpatterns = [
    path('',views.HotelAPI.as_view()), # GET request : http://localhost:8000/hotel/

]