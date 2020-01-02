from django.test import TestCase
from . models import Movie
from django.contrib.auth.models import User


class MovieTest(TestCase):
    def setUp(self):
        pass

    def test_movie_create(self):
        """ Test if Movie objects can be created """
        all_users = User.objects.all()
        print('All users are : ', all_users)
        # movie_owner = User.objects.get(pk=2)
        # movie_obj = Movie.objects.create(owner=movie_owner, movie_name='Avengers', movie_description="Something", movie_imdb=9.0)
        #
        # self.assertEqual(movie_obj.owner, 2)
        # self.assertEqual(movie_obj.movie_name, 'Avengers')