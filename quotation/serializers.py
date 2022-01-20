from rest_framework import serializers
from .models import Quotation


class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = ['name', 'email', 'subject', 'service', 'message', 'date']
