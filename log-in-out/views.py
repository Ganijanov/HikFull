from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def login_users(request):
    username = request.request.data['username']
    password = request.request.data['password']
    chek = authenticate(username=username, password=password)
    if chek is not None:
        login(request, chek)
        if chek.is_superuser == True:
            data = 'index_boss_url'
        else:
            data = 'index_url'
        return 
    else:
        return 
    








@api_view(["GET"])
def logout(request):
    return
def  logoutForAdmin(request):
    logout(request)
    return     ('kitchen_index_url')