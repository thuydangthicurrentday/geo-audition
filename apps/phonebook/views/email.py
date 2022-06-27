from rest_framework.viewsets import ModelViewSet
from apps.phonebook.models import Email
from apps.phonebook.serializers import *


class EmailViewSet(ModelViewSet):
    """
    A viewset for viewing and editing Email instances.
    """
    serializer_class = EmailSerializer
    queryset = Email.objects.all()
