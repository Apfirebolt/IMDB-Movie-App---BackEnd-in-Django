from django.shortcuts import render


def movie_home(request):
    return render(request, 'movies/movie_home.html', {})
