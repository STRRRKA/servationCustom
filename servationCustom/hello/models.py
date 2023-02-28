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

class User(models.Model):
    name = models.CharField(max_length=20)
    familia = models.CharField(max_length=20)
    otchestvo = models.CharField(max_length=20)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mail = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    birthday = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=30)

class Hall(models.Model):
    capacity = models.IntegerField()

class Session(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False)
    hall = models.OneToOneField(Hall, on_delete = models.CASCADE)
    movie = models.OneToOneField(Movie, on_delete = models.CASCADE)
    date = models.DateField()
    time = models.TimeField()