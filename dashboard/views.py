# B.R.R
from django.http import HttpResponse
from django.shortcuts import render
from main import models
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required


@api_view(['GET'])
def list_users(request):
    users = models.IqroUser.objects.all()
    serializer = serializers.ListUserSer(users, many= True)
    return Response(serializer.data)


# @login_required()
@api_view(['POST'])
def create_user(request):
    if request.user.is_superuser:
        try:
            models.IqroUser.objects.create(
            username = request.data['username'],
            password = request.data['password'],
            email = request.data['email'],
            is_active = True,
            is_staff = True if request.data['is_staff'] == 'True'else False,
            first_name = request.data['first_name'],
            last_name = request.data['last_name'],
            s_name = request.data['s_name'],#Father name (Otasini ismi)
            phone_num = request.data['phone_number'],
            
            type = request.data['type'],#( 1,"Super"),(2,'admin'),(3,'head teacher'),(4,'teacher')
            birthday = request.data['bithday'],
            passport_ser = request.data['passport_seria'],
            passport_JSHSHR = request.data['jshshr'],
            finger_id = "3",
            telegram = "1",
            )
            res = {'status':'Created'}
        except:
            res = {'status':'Samething get wrong'}
    else:
        res = {'status':'You have access:('}
    return Response(res)

@api_view(['PUT'])
def upgruser(request):
    if request.user.is_superuser:
        user = models.IqroUser.objects.get(id=request.data['id'])
        print(user.last_name)
        try:
            user.username = request.data['username'],
            user.password = request.data['password'],
            user.email = request.data['email'],
            user.is_active = True,
            user.is_staff = True if request.data['is_staff'] == '1' else False,
            user.first_name = request.data['first_name'],
            user.last_name = request.data['last_name'],
            user.s_name = request.data['s_name'],#Father name (Otasini ismi)
            user.phone_num = request.data['phone_number'],
            
            user.type = request.data['type'],#( 1,"Super"),(2,'admin'),(3,'head teacher'),(4,'teacher')
            user.birthday = request.data['bithday'],
            user.passport_ser = request.data['passport_seria'],
            user.passport_JSHSHR = request.data['jshshr'],
            user.finger_id = "1",
            user.telegram = "2",
            user.save()
            print(user)  
            res = {'status':'Created'}
        except:
            res = {'status':'Samething get wrong'}
    else:
        res = {'status':'You have access:('}
    return Response(res)