from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 45)
    genre = models.CharField(max_length = 45, null = True)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)