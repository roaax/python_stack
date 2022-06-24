from django.db import models
import re
import bcrypt
import datetime



#  ------------- Login & Registration validation | User Model --------------------
class UserManager(models.Manager):
    def register_validation(self,postData):
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

        if postData['password'] != postData['confirm_password']:
            errors["passwords"] = "passwords are not matched!" 

        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters" 
        
        return errors

    def login_validation(self,postData):
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
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateTimeField(default="1999-01-01")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# --------------Book class Model and Validation
class BookManager(models.Manager):
    def book_validator(self,postData):
        errors = {}
        if len(postData['title'])<1:
            errors['title']="You must include the title."
        if len(postData['description'])<5:
            errors['description']="Your description must be at least 5 characters."
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User,related_name="book_uploader",on_delete=models.CASCADE)
    users_who_like =models.ManyToManyField(User, related_name="liked_books")
    objects = BookManager()


# ----------------- not on assignment----------
class CommentManager(models.Manager):
    def comment_validtor(self, postData):
        errors = {}
        if len(postData['comment']) < 2:
            errors['comment'] = "Comment must be more than 2 characters"

        return errors

class Comment(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CommentManager()
    book_comments = models.ForeignKey(Book,related_name="comments",on_delete=models.CASCADE)
    who_comment = models.ForeignKey(User,related_name="comments",on_delete=models.CASCADE)