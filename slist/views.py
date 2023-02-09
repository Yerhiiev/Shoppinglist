from django.shortcuts import render
from django.http import HttpResponse
from models import Shoppinglist, UserList, Mallist, Item

# Create your views here.
def index(request):
    user_list = UserList.objects.filter(user_id=1).first()
    result = Shoppinglist.objects.filter(list_id=user_list.list_id)
    result.filter()
    return HttpResponse("Hello it's shopp inglist")

def add_item(request):
    return HttpResponse("Add Item")

def buy_item(request, item_id):
    return HttpResponse("Buy Item")

def remove_item(request, item_id):
    return HttpResponse("Remove Item")

