from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class TicketCinema(models.Model):
    ticketNumber = models.IntegerField()
    sessionNumber = models.IntegerField()
    placeNumber = models.IntegerField()
    servation = models.IntegerField()

class Reserved(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False)
    # userID = model.

class Movie(models.Model):
    name = models.CharField(max_length=30)

class Hall(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False)
    capacity = models.IntegerField()
    scheme = models.CharField(max_length=1000)

class Session(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False)
    hall = models.OneToOneField(Hall, on_delete = models.CASCADE)
    movie = models.OneToOneField(Movie, on_delete = models.CASCADE)
    date = models.DateField()
    time = models.TimeField()