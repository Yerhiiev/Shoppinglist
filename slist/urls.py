from django.urls import path

from . import views


urlpatterns = [
    path('', views.user, name='user'),
    path('shop', views.add_shop, name='add_shop'),
    path('user', views.add_user, name='add_user'),
    path('analytics', views.analytics, name='analytics'),
    path('index', views.index, name='index'),
    path('add', views.add_item, name='add_item'),
    path('<item_id>/buy', views.add_item, name='buy_item'),
    path('<item_id>/remove', views.add_item, name='remove_item')
]
