from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from apps.phonebook.models import Phonebook
from apps.phonebook.serializers import PhonebookSerializer


class PhonebookViewSet(ModelViewSet):
    queryset = Phonebook.objects.all()
    serializer_class = PhonebookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'phone_numbers__phone_number']
