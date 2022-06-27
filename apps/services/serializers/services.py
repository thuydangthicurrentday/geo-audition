from apps.services.models import Service
from rest_framework import serializers

class ServiceSerializer(serializers.ModelSerializer):
    """
    Serializer class of Service api
    """
    class Meta:
        model = Service
        fields = '__all__'
