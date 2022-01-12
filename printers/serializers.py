from rest_framework import serializers
from .models import Printer, Requestment


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = '__all__'
        read_only_fields = ['requestment', 'state']


class RequestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requestment
        fields = '__all__'
        read_only_fields = ['author', 'state']
