from django.db import models

# Create your models here.
class Movie(models.Model):
<<<<<<< HEAD
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
=======
  title=models.CharField(max_length=20)
  audience=models.IntegerField()
  release_data=models.DateField()
  genre=models.CharField(max_length=30)
  score=models.FloatField()
  poster_url=models.TextField()
  description=models.TextField()
>>>>>>> d91e101d9b9fccd0ec02132f6b839b5d2dcb06bf
