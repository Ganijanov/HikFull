from django.shortcuts import render
from main import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
# from . import serializers


@api_view(["GET"])
# def list_users(request):
#     users= models.IqroUser.objects.all()
#     serializer = serializers.ListUserSer(users, many=True)
#     return Response(serializer.data)

def create_iqro_user(request):
    models.IqroUser.objects.create(
    username = 5,
    email = None,
    is_active = 1,
    is_staff = 0,
    first_name = 'S',
    last_name = 's',
    s_name = None,
    phone_num = 1212,
    
    type = 1,
    birthday = '2001-02-02',
    passport_ser = 35,
    passport_JSHSHR = 22656,
    finger_id = '122233',
    telegram = 258,

    )
    return Response(True)