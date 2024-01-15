from rest_framework import serializers
from main import models

class ListUserSer(serializers.ModelSerializer):
    class Meta:
        model = models.IqroUser
        fields = "__all__"
        

class SchoolSer(serializers.ModelSerializer):
    class Meta:
        model = models.School
        fields = "__all__"