from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'api', views.MovieViewSet, basename='movie-api')

urlpatterns = [
    path('', views.movie_home, name='home'),
]

urlpatterns += router.urls