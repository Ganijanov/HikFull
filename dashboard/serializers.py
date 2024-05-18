from rest_framework import serializers
from main import models

class ListUserSer(serializers.ModelSerializer):
    class Meta:
        model = models.IqroUser
        fields = "__all__"
        

class SubSer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = "__all__"


class SchoolSer(serializers.ModelSerializer):
    class Meta:
        model = models.School
        fields = "__all__"


class ClasSer(serializers.ModelSerializer):
    class Meta:
        model = models.Cla_ss
        fields = "__all__"


class ListPerSer(serializers.ModelSerializer):
    class Meta:
        model = models.Parent
        fields = "__all__"



class ListPupSer(serializers.ModelSerializer):
    class Meta:
        model = models.Pupil
        fields = "__all__"


class ListPaySer(serializers.ModelSerializer):
    class Meta:
        model = models.PayHis
        fields = "__all__"
        

class SaleHisList(serializers.ModelSerializer):
    class Meta:
        model = models.SaleHis
        fields = "__all__"
        

class SalHisList(serializers.ModelSerializer):
    class Meta:
        model = models.SalHis
        fields = "__all__"
        

class ChiqLsSer(serializers.ModelSerializer):
    class Meta:
        model = models.Chiq
        fields = "__all__"




