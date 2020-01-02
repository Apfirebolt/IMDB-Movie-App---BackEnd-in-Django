from . models import Movie
from rest_framework import serializers
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Movie
        fields = ('owner', 'movie_name', 'movie_description', 'movie_imdb', 'created_at',)

