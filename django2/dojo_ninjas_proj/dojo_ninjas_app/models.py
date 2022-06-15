from django.db import models


# Create your models here.
class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state= models.CharField(max_length=2)
    desc=models.TextField(default='old dojo')

    def __str__(self):
        return f"name: {self.name} | city: {self.city} | state: {self.state} "
class Ninjas(models.Model):
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo_id = models.ForeignKey(Dojos, related_name="dojo", on_delete = models.CASCADE)
