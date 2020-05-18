from django.urls import path
from . import views

urlpatterns = [
    path('first-route', views.first_view),
    path('second-route', views.second_view)
]