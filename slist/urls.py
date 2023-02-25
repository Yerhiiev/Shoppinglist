from django.urls import path

from . import views


urlpatterns = [
    path('/', views.index, name='index'),
    path('/user', views.user, name='user'),
    path('/shop', views.add_shop, name='add_shop'),
    path('/add_user', views.add_user, name='add_user'),
    path('/analytics', views.analytics, name='analytics'),
    path('/<item_id> <quantity>/buy', views.buy_item, name='buy_item'),
    path('/<item_id>/remove', views.remove_item, name='remove_item')
]
