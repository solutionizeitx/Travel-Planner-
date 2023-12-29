from django.urls import path

from BookingApp import views

urlpatterns = [
    path('',views.BookingAPI.as_view()), # GET request : http://localhost:8000/booking/

]