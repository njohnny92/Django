from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def user_validations(self, postData):
        errors = {}
        NAME_REGEX = re.compile(r'^[a-zA-Z]')
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

        #first name validation
        if len(postData['firstname']) == 0:
            errors['firstname'] = 'First name section cannot be empty.'
        elif not NAME_REGEX.match(postData['firstname']):
            errors['firstname'] = 'First name must only contain letters.'
        elif len(postData['firstname']) < 2:
            errors['firstname'] = 'First name must at least consist of two characters or more.'

        #last name validation
        if len(postData['lastname']) == 0:
            errors['lastname'] = 'Last name section cannot be empty.'
        elif not NAME_REGEX.match(postData['lastname']):
            errors['lastname'] = 'Last name must only contain letters.'
        elif len(postData['lastname']) < 2:
            errors['lastname'] = 'Last name must at least consist of two characters or more.'

        #email validation
        if len(postData['email']) == 0:
            errors['email'] = 'Email field cannot be empty.'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid Email Address.'

        #password validation
        if len(postData['password']) == 0:
            errors['password'] = 'Please include a password.'
        if postData['password'] != postData['confirm'] or len(postData['confirm']) == 0:
            errors['confirm'] = 'Unmatched passwords.'

        #one user validation
        for user in User.objects.filter(email = postData['email']):
            if user is not None:
                errors['same_user'] = 'This email has already been registered.'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField()
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name = 'books_uploaded', on_delete = models.CASCADE)
    user_likes = models.ManyToManyField(User, related_name = 'liked_books')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)