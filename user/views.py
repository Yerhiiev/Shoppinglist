from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import uuid
from slist.models import UserList


def index(request):
    return HttpResponse("user")

def user_invite(request):
    if not request.user.is_authenticated:
        return HttpResponse('You are already logged in')
    if request.method == 'GET':
        return render(request, 'invite.html')

    email = request.POST.get('email')
    invited_user = User.objects.filter(email=email).first()
    if invited_user is None:
        return HttpResponseNotFound('User not found')
    invited_user_list = UserList.objects.filter(user_id=invited_user.id).first()
    current_user_list = UserList.objects.filter(user_id=request.user.id).first()
    invited_user_list.list_id = current_user_list.list_id
    invited_user_list.save()
    return HttpResponse(f'user {invited_user.first_name} {invited_user.email} invited')

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponse('You are already logged in')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('logged in')
        else:
            return HttpResponse('not logged in')
    else:
        return render(request, 'login.html')


def user_register(request):
    if request.user.is_authenticated:
        return HttpResponse('You are already logged in')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username, email, password)
        user.save()
        user_list = UserList(user_id=user.id, list_id=uuid.uuid4())
        user_list.save()
        return redirect('/user/login')

    return render(request, 'register.html')


def user_logout(request):
    logout(request)
    return redirect('/user/login')
