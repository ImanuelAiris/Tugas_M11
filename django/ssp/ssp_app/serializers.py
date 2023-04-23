from rest_framework import serializers
from .models import Sistem1, Sistem2, Sistem3
    
class Sistem1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sistem1
        fields = "__all__"

class Sistem2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sistem2
        fields = "__all__"

class Sistem3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Sistem3
        fields = "__all__"