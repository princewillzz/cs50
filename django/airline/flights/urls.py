from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("<int:flight_id>", views.flight)
]