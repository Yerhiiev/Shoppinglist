from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from .models import Shoppinglist, UserList, Mallist, Item
from django.contrib.auth.models import User


def index(request):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    user_list = UserList.objects.filter(user_id=1).first()
    if request.method == 'POST':
        item_name = request.POST.get('item')
        quantity = request.POST.get('quantity')
        shop_id = request.POST.get('shop')
        shop_object = Mallist.objects.filter(pk=shop_id).first()
        item_object = Item(name=item_name, shop_id=shop_object)
        item_object.save()

        new_item = Shoppinglist(list_id=user_list.list_id, item_id=item_object, quantity=quantity)
        new_item.save()

    result = list(Shoppinglist.objects.filter(list_id=user_list.list_id).all())

    return render(request, 'item_form.html',
                  {'shopping_list_data': result,
                   'shops': Mallist.objects.all().filter(list_id=user_list.list_id),
                   'items': Item.objects.all()})


def buy_item(request, item_id, quantity):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    if request.method == 'POST':
        user_list = UserList.objects.filter(user_id=1).first()
        price = request.POST.get('price')
        status = 'bought'
        buy_date = request.POST.get('buy_date')
        change_item = Shoppinglist(list_id=user_list.list_id, item_id_id=item_id,
                                   price=price, status=status, buy_date=buy_date,
                                   quantity=quantity)
        change_item.save()

    return redirect('/shopping_list/')

def remove_item(request, item_id):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    if request.method == 'POST':
        item_object = Item.objects.filter(id=item_id)
        item_object.delete()

    return redirect('/shopping_list/')

def user(request):
    return HttpResponse("User")

def add_shop(request):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    if request.user.is_authenticated:
        if request.method == 'POST':
            mall_list = UserList.objects.filter(user_id=1).first()
            shop = request.POST.get('shop')
            shop_object = Mallist(name=shop, list_id=mall_list.list_id)
            shop_object.save()

        return redirect('/shopping_list/')
def add_user(request, user_id):
    return HttpResponse("Add User")

def analytics(request):
    return HttpResponse("Analytics")
