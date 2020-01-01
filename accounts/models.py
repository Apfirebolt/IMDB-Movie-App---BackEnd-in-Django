from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_description = models.TextField()
    movie_actors = models.CharField(max_length=100)
    movie_imdb = models.FloatField()
    production_house = models.CharField(max_length=50)

    def __str__(self):
        return str(self.movie_name) + ' - ' + str(self.movie_imdb)





