from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from apps.services.models import Service
from apps.services.serializers import ServiceSerializer


class ServiceViewSet(ModelViewSet):
    """
    A viewset for viewing and editing Service instances.
    """
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
