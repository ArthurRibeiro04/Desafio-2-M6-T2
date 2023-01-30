from rest_framework import serializers
from .models import Operation
import ipdb

class OperationSerializer(serializers.Serializer):
    Transaction_type = serializers.CharField()
    Data = serializers.CharField()
    Value = serializers.CharField()
    CPF = serializers.CharField()
    Card = serializers.CharField()
    Time = serializers.CharField()
    Owner = serializers.CharField()
    Shop_name = serializers.CharField()
    
    def create(self, validated_data):
        saida = ["2", "3", "9"]
        
        if(validated_data["Transaction_type"] in saida):
            validated_data["Transaction_type"] = "Saída"
        else:
            validated_data["Transaction_type"] = "Entrada"
            
        operation = Operation.objects.create(**validated_data)
        
        
        return operation
        