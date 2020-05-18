from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def user_validations(self, postData):
        errors = {}
        NAME_REGEX = re.compile(r'^[a-zA-Z]')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        #email validations
        if len(postData['email']) == 0:
            errors['email'] = 'Email field cannot be empty.'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid Email Address.'

        #first name validations
        if len(postData['firstname']) == 0:
            errors['firstname'] = 'First name cannot be empty.'
        elif not NAME_REGEX.match(postData['firstname']):
            errors['firstname'] = 'First name must contain only letters.'
        elif len(postData['firstname']) < 2:
            errors['firstname'] = 'First name must consist more than 2 characters.'

        #last name validations
        if len(postData['lastname']) == 0:
            errors['lastname'] = 'Last name cannot be empty.'
        elif not NAME_REGEX.match(postData['lastname']):
            errors['lastname'] = 'Last name must contain only letters.'
        elif len(postData['lastname']) < 2:
            errors['lastname'] = 'Last name must consist more than 2 characters.'

        #password validations
        if len(postData['password']) < 8:
            errors['password'] = 'Password must contain 8 characters or more.'
        if postData['confirm'] != postData['password']:
            errors['confirm'] = 'Passwords must match.'

        #one user validation
        for user in User.objects.filter(email=postData['email']):
            if user is not None:
                errors['same_email'] = 'This email has already been registered.'

        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name = 'messages', on_delete = models.CASCADE, blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message, related_name = 'comments', on_delete = models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, related_name = 'comments', on_delete = models.CASCADE, blank = True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)