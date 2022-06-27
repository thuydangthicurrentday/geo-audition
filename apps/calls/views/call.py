from rest_framework.viewsets import ModelViewSet
from apps.calls.models import Call
from apps.calls.serializers import CallSerializer


class CallViewSet(ModelViewSet):
    """
    A viewset for viewing and editing Call instances.
    """
    serializer_class = CallSerializer
    queryset = Call.objects.all()
    filterset_fields = ['user_phone_number__phonebook__id', 'user_phone_number__phone_number', 'switchboard_phone_number__id']
