from rest_framework import serializers
from main import models

class ListUserSer(serializers.ModelSerializer):
    class Meta:
        model = models.IqroUser
        fields = "__all__"