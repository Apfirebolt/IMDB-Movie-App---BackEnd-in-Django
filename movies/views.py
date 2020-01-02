from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from . models import Movie
from django.shortcuts import get_object_or_404
from . serializers import MovieSerializer
from rest_framework import status


def movie_home(request):
    return render(request, 'movies/movie_home.html', {})


class MovieViewSet(viewsets.ViewSet):
  """
  A simple ViewSet for listing or retrieving movies.
  """

  def create(self, request):
      post_data = request.data
      movie_obj = Movie()
      movie_obj.owner = User.objects.get(pk=post_data['owner'])
      movie_obj.movie_name = post_data['movie_name']
      movie_obj.movie_description = post_data['movie_description']
      movie_obj.movie_imdb = post_data['movie_imdb']
      movie_obj.save()
      return Response(status=status.HTTP_201_CREATED)

  def list(self, request):
      queryset = Movie.objects.all()
      serializer = MovieSerializer(queryset, many=True)
      return Response(serializer.data)

  def retrieve(self, request, pk=None):
      queryset = Movie.objects.all()
      user = get_object_or_404(queryset, pk=pk)
      serializer = MovieSerializer(user)
      return Response(serializer.data)
