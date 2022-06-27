from rest_framework import serializers
from apps.switchboard.models import Switchboard


class SwitchboardSerializer(serializers.ModelSerializer):
    """
    Serializer class of Switchboard api
    """
    class Meta:
        model = Switchboard
        fields = '__all__'
