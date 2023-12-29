from django.urls import path

from UserApp import views

urlpatterns = [
    # GET request : http://localhost:8000/User/
    path('', views.UserAPI.as_view()),
    path('login/', views.UserLoginAPI.as_view()),

]
