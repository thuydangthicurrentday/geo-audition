from django.db import transaction
from rest_framework import serializers
from apps.phonebook.models import Phonebook, Email, PhoneNumber
from apps.phonebook.serializers.email import EmailNestedSerializer
from apps.phonebook.serializers.phone_number import PhoneNumberNestedSerializer


class PhonebookSerializer(serializers.ModelSerializer):
    """
    Serializer class of Phonebook api
    """
    phone_numbers = PhoneNumberNestedSerializer(many=True, required=True)
    emails = EmailNestedSerializer(many=True, required=False)

    class Meta:
        model = Phonebook
        fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        phone_numbers_data = validated_data.pop('phone_numbers', [])
        emails_data = validated_data.pop('emails', [])
        phonebook = Phonebook.objects.create(**validated_data)
        for phone_number_data in phone_numbers_data:
            PhoneNumber.objects.create(phonebook=phonebook, **phone_number_data)
        for email_data in emails_data:
            Email.objects.create(phonebook=phonebook, **email_data)
        return phonebook
