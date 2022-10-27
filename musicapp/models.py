from datetime import datetime
from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=40)
    Last_name = models.CharField(max_length=40)
    Age = models.IntegerField()

class Song(models.Model):
    Artiste = models.ForeignKey('Artiste', on_delete=models.CASCADE)
    Title =models.TextField(max_length=400)
    Date_released = models.DateTimeField(default=datetime.today)
    Likes = models.IntegerField()
    artiste_code = models.IntegerField()

    
class Lyrics(models.Model):
   Song = models.ForeignKey(Song, on_delete=models.CASCADE)
   Content = models.TextField(max_length=400)
   song_code = models.IntegerField()
