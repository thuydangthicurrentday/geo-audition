from rest_framework import serializers
from apps.calls.models import Call


class CallSerializer(serializers.ModelSerializer):
    """
    Serializer class of Call api
    """
    class Meta:
        model = Call
        fields = '__all__'
