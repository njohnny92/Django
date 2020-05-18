from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.render_create),
    path('create', views.process_create),
    path('shows/<int:show_id>', views.render_read),
    path('shows/<int:show_id>/edit', views.render_update),
    path('update/<int:show_id>', views.process_update),
    path('shows/<int:show_id>/delete', views.process_delete)
]
