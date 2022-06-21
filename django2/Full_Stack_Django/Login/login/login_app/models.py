from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def registration_validator(self,postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors['fname'] = "First Name must be more than 2 characters "

        if len(postData['lname']) < 2:
            errors['lname'] = "Last Name must be more than 2 characters "

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is not valid"
        else:
            try:
                user = User.objects.get(email__iexact=postData['email'])
                errors['email'] = "Email is already registered try to login!"  
            except:
                pass
        
        if postData['password'] != postData['cPassword']:
            errors["passwords"] = "passwords are not matched!" 

        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters" 
        
        return errors

    def login_validator(self,postData):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email is not valid"
        else:
            try:
                user = User.objects.get(email__iexact=postData['email'])
                if not bcrypt.checkpw(postData['password'].encode(),user.password.encode()):
                    errors['login'] = "Email or Password is incorrect !"
            except:
                errors['login'] = "Email or Password is incorrect !"
        
        return errors

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

