from __future__ import unicode_literals
from datetime import date, datetime
from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        #instantiate today as today's date.
        today = date.today()
        #instantiate input_date as user's input date and convert the string into datetime.datetime format then .date() converts it into datetime.date format
        input_date = datetime.strptime(postData['release'], '%Y-%m-%d').date()
        if len(postData['title']) < 2:
            errors['title'] = 'Title must at least be 2 characters long!'
        if len(postData['net']) < 3:
            errors['net'] = 'Network must be at least 3 characters long!'
        if len(postData['desc']) < 10:
            errors['desc'] = 'Description must be at least 10 characters long!'
        #compare the input_date's to today's date
        if input_date > today:
            errors['release'] = 'Release date must be in the past!'
        for show in Show.objects.filter(title = postData['title']):
            if show:
                errors['repeated'] = 'This title already exists.  Please use a different one.'
        return errors

class Show(models.Model):
    title = models.CharField(max_length = 45)
    network = models.CharField(max_length = 45)
    description = models.TextField(max_length = 45)
    release = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()