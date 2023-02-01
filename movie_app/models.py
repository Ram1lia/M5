from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=200)

class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    duration = models.FloatField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

class Review(models.Model):
    text = models.TextField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)




