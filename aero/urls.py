from django.urls import path
from . import views


# Creates a url path with the given name in the quotes like facebook.com/about

urlpatterns = [
    path('', views.home),
]
