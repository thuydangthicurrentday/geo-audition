from rest_framework.viewsets import ModelViewSet
from apps.phonebook.models import PhoneNumber
from apps.phonebook.serializers import PhoneNumberSerializer


class PhoneNumberViewSet(ModelViewSet):
    """
    A viewset for viewing and editing PhoneNumber instances.
    """
    serializer_class = PhoneNumberSerializer
    queryset = PhoneNumber.objects.all()
