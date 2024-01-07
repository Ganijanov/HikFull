from rest_framework import serializers
from main import models

class FingerPrintSer(serializers.ModelSerializer):

    class Meta:
        model = models.Finger_Print
        fields = ('id', 'arrived', 'left', 'users', 'pupil')


class ListUserSer(serializers.ModelSerializer):

    class Meta:
        model = models.IqroUser
        exclude = ['password', 'groups', 'user_permissions', 'last_login', 'is_active', 'is_staff','is_superuser']