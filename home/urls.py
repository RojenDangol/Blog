from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('search', views.search, name="search"),
    path('signup', views.handleSignup, name="handle signup"),
    path('login', views.handleLogin, name="handle login"),
    path('logout', views.handleLogout, name="handle logout"),
]
