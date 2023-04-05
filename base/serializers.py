from rest_framework import serializers
from .models import PincodeData

# class MyModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PincodeData
#         fields = '__all__'


class PincodeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PincodeData
        fields = "__all__"