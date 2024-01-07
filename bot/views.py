from django.shortcuts import render
from main import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from . import serializers


@api_view(["GET"])
def list_turniket_users(request):
    person = models.IqroUser.objects.get(id=request.data['id'])
    users = models.Finger_Print.objects.filter(users=person)
    serializer = serializers.FingerPrintSer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_turniket_pupil(request):
    person = models.Pupil.objects.get(id=request.data['id'])
    pupil = models.Finger_Print.objects.filter(pupil=request.data['id'])
    serializer = serializers.FingerPrintSer(pupil, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def arrived_left_person(request):
    try:
        person = models.Pupil.objects.get(finger_id=request.data['finger_id'])
        attendance, created = models.Finger_Print.objects.get_or_create(pupil=person, left__isnull=True)
        if created:
            attendance.arrived = datetime.now()
            attendance.save()
            data = 'Зафиксирован приход'
        else:
            try:
                attendance = models.Finger_Print.objects.get(pupil=person, arrived__isnull=False, left__isnull=True)
                attendance.left = datetime.now()
                attendance.save()
                data = 'Зафиксирован уход'
            except models.Finger_Print.DoesNotExist:
                data = 'Пользователь не зарегистрировал приход'
    except:
        person = models.IqroUser.objects.get(finger_id=request.data['finger_id'])
        attendance, created = models.Finger_Print.objects.get_or_create(users=person, left__isnull=True)
        if created:
            attendance.arrived = datetime.now()
            attendance.save()
            data = 'Зафиксирован приход'
        else:
            try:
                attendance = models.Finger_Print.objects.get(users=person, arrived__isnull=False, left__isnull=True)
                attendance.left = datetime.now()
                attendance.save()
                data = 'Зафиксирован уход'
            except models.Finger_Print.DoesNotExist:
                data = 'Пользователь не зарегистрировал приход'
    return Response({'status':data})
