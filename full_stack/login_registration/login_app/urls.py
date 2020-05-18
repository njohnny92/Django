from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('success', views.login),
    path('register', views.process_register),
    path('login', views.process_login),
    path('logout', views.process_logout)
]