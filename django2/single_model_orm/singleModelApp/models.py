from django.db import models

# Create your models here.

class User(models.Model):
    # id
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255)
    email_address =  models.CharField(max_length=255)
    age =  models.IntegerField()
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<User object: First Name: {self.first_name} | Last Name: {self.last_name} | Email Address: {self.email_address} | Age: ({self.age})| Created At: ({self.created_at}) | Updated At: ({self.updated_at}) >"