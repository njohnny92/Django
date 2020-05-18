from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
import re

# Create your models here.
class UserManager(models.Manager):
    def user_validations(self, postData):
        errors = {}
        today = date.today()
        #input_date = datetime.strptime(postData['birthdate'], '%Y-%m-%d').date()
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email Address!"
        if len(postData['firstname']) == 0:
            errors['firstname'] = 'First name cannot be empty.'
        elif len(postData['firstname']) < 2:
            errors['firstname'] = 'First name must be at least 2 characters long!'
        if len(postData['lastname']) == 0:
            errors['lastname'] = 'Last name cannot be empty.'
        elif len(postData['lastname']) < 2:
            errors['lastname'] = 'Last name must be at least 2 characters long!'
        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long!'
        if postData['confirm'] != postData['password']:
            errors['confirm'] = 'Passwords must match!'
        # if input_date > today:
        #     errors['birthdate'] = 'Birthdate must be in the past!'
        for user in User.objects.filter(email=postData['email']):
            if user is not None:
                errors['same_email'] = 'This email has already been taken! Please choose a different email.'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()