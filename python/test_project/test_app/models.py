from django.db import models

# Create your models here.

class UserModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length = 30)
    email = models.CharField(max_length=255)
    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email
    def fetch_all_data(self):
        return "Your name is " + self.first_name + " " + self.last_name + " " + self.email

class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument_name = models.CharField(max_length=255)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    users = models.ManyToManyField(UserModel, verbose_name="Access to Multiple Users")


class Person(models.Model):
    SHIRT_SIZES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large"
    }
    name=models.CharField(max_length=60)
    shirt_size=models.CharField(max_length=1, choices=SHIRT_SIZES)

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)