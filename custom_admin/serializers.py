from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'

class InvoiceSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = invoice
        fields = '__all__'