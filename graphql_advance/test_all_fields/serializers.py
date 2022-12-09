from rest_framework import serializers
from .models import TestAllFields


class TestAllFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAllFields
        fields = "__all__"






