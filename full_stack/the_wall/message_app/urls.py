from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('wall', views.wall),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('message', views.post_message),
    path('comment', views.post_comment),
    path('delmsg/<int:message_id>', views.delete_message),
    path('delcmt/<int:comment_id>', views.delete_comment)
]