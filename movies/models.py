from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Movie(models.Model):
    owner = models.ForeignKey(get_user_model(), related_name='saved_movies', on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=100)
    movie_description = models.TextField()
    movie_imdb = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.movie_name) + ' - ' + str(self.movie_imdb)