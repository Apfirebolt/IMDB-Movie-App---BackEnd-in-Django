from django.urls import path
from rest_framework.authtoken import views as auth_token_view
from . import views

urlpatterns = [
    path('api-token-auth', auth_token_view.obtain_auth_token),
    path('create', views.CreateUserView.as_view(), name='create'),
    path('list', views.ListUserView.as_view(), name='user-list'),
    ]
