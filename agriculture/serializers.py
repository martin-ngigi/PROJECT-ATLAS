from rest_framework import serializers
from models import  AgricultureRecord

class AgricultureSerializer(serializers.Serializer):
    class Meta:
        model = AgricultureRecord
        fields = '__all__'
