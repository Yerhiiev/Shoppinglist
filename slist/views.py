from django.shortcuts import render
from django.http import HttpResponse
from .models import Shoppinglist, UserList, Mallist, Item

def index(request):
    user_list = UserList.objects.filter(user_id=1).first()
    result = Shoppinglist.objects.filter(list_id=user_list.list_id)
    new_result = [itm.__dict__ for itm in result]
    result.filter()
    return HttpResponse(str(new_result))

def add_item(request):
    return HttpResponse("Add Item")

def buy_item(request, item_id):
    return HttpResponse("Buy Item")

def remove_item(request, item_id):
    return HttpResponse("Remove Item")

def user(request):
    return HttpResponse("User")

def add_shop(request, shop_id):
    return HttpResponse("Add Shop")

def add_user(request, user_id):
    return HttpResponse("Add User")

def analytics(request):
    return HttpResponse("Analytics")
