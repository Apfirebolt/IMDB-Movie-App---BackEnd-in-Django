from django.urls import path
from rest_framework.authtoken import views as auth_token_view
from . import views

urlpatterns = [
    path('api-token-auth', views.CustomObtainAuthToken.as_view(), name='token-auth'),
    path('create', views.CreateUserView.as_view(), name='create'),
    path('list', views.ListUserView.as_view(), name='user-list'),
    ]
