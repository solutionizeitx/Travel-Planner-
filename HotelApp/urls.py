from django.urls import path

from HotelApp import views

urlpatterns = [
    # GET request : http://localhost:8000/hotel/
    path('', views.HotelAPI.as_view()),
    path('type/', views.HotelTypeAPI.as_view()),

]
