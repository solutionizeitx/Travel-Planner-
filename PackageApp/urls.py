from django.urls import path

from PackageApp import views

urlpatterns = [
    path('',views.PackageAPI.as_view()), # GET request : http://localhost:8000/package/

]