from django.urls import path

from . import views


urlpatterns = [
    path('/login', views.user_login, name='index'),
    path('/invite', views.user_invite, name='user_invite'),
    path('/register', views.user_register, name='user_register'),
    path('/logout', views.user_logout, name='logout'),
]