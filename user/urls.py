from django.urls import path

from . import views


urlpatterns = [
    path('/login', views.user_login, name='index'),
    path('/register', views.user_register, name='user_register'),
    path('/logout', views.user_logout, name='logout'),
]