from django.urls import path

from PackageApp import views

urlpatterns = [
    # GET request : http://localhost:8000/package/
    path('', views.PackageAPI.as_view()),
    path('type/', views.PackageTypeAPI.as_view()),


]
