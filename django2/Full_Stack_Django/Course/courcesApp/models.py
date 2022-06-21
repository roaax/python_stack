from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len (postData['name'])<5:
            errors['name']='Name cannot be less than 5 characters!'
        
        if len (postData['desc'])<15:
            errors['desc']='Description cannot be less than 15 characters!'
        return errors

class Course(models.Model):
    name=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= CourseManager()

class Comment(models.Model):
    comment=models.CharField(max_length=255)
    course=models.ForeignKey(Course, related_name='comments',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)