from django.urls import path

from . import views
urlpatterns = [
    path('', views.easter_egg)
]