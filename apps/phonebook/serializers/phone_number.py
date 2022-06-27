from rest_framework import serializers
from apps.phonebook.models import PhoneNumber


class PhoneNumberNestedSerializer(serializers.ModelSerializer):
    """
    Serializer class of PhoneNumber api
    """
    class Meta:
        model = PhoneNumber
        fields = ['id', 'phone_number']
        extra_kwargs = {'id': {'read_only': True}}


class PhoneNumberSerializer(serializers.ModelSerializer):
    """
    Serializer class of PhoneNumber api
    """
    class Meta:
        model = PhoneNumber
        fields = ['id', 'phone_number', 'phonebook']
        extra_kwargs = {'id': {'read_only': True}}
