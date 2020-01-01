from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('api/', include(('accounts.api.urls', 'accounts.api'), namespace='accounts-api')),
    # path('register/', views.RegisterForm.as_view(), name='register'),
    # path('settings/<int:pk>', views.EditAccountSettings.as_view(), name='settings'),
    # path('login/', views.accounts_login, name='login'),
    # path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home_view, name='home'),
]