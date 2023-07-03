from django.db import models
class Artist(models.Model):
    gender = (
        ("male", "Male"),
        ("female", "Female"),
    )
    name = models.CharField(max_length=255)
    sex = models.CharField(choices=gender, max_length=255)

class Track(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField(default=0)
# Create your models here.
class Album(models.Model):
    song_type =(
        ("pop", "Pop"),
        ("afro","Afro"),
        ("soul", "Soul"),
    )
    
    title = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(choices=song_type, max_length=255)
    description = models.TextField(blank=True, max_length=255)
    likes = models.IntegerField(default=0)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    

