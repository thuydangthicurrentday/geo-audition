from rest_framework import serializers
from apps.phonebook.models import Email


class EmailNestedSerializer(serializers.ModelSerializer):
    """
    Serializer class of Email api
    """
    class Meta:
        model = Email
        fields = ['email', 'id']
        extra_kwargs = {'id': {'read_only': True}}


class EmailSerializer(serializers.ModelSerializer):
    """
    Serializer class of Email api
    """
    class Meta:
        model = Email
        fields = ['email', 'id']
        extra_kwargs = {'id': {'read_only': True}}
