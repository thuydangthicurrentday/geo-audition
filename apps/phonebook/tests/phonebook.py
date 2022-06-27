import json
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from apps.phonebook.models import Phonebook
from apps.phonebook.serializers import PhonebookSerializer


client = Client()


class GetAllPhonebookTest(TestCase):
    """ Test module for GET all phonebook API """

    def setUp(self):
        Phonebook.objects.create(
            name='Customer 1', description='')
        Phonebook.objects.create(
            name='Customer 2', description='')

    def test_get_phonebook(self):
        response = client.get(reverse('phonebook'))
        phonebook = Phonebook.objects.all()
        serializer = PhonebookSerializer(phonebook, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePhonebookTest(TestCase):
    """ Test module for GET single phonebook API """

    def setUp(self):
        Phonebook.objects.create(
            name='Customer 1', description='')
        Phonebook.objects.create(
            name='Customer 2', description='')
        Phonebook.objects.create(
            name='Customer 3', description='')

    def test_get_valid_single_customer(self):
        customer_id = 2
        response = client.get(
            reverse('phonebook', kwargs={'pk': customer_id}))
        customer = Phonebook.objects.get(pk=customer_id)
        serializer = PhonebookSerializer(customer)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_customer(self):
        response = client.get(
            reverse('phonebook', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreatePhonebookTest(TestCase):
    """ Test module for add new customer to phonebook API """

    def setUp(self):
        self.valid_payload = {
            'name': 'Customer 1', 
            'description': None,
            'phone_numbers': [{
                'phone_number': '0123456'
            }]
        }
        self.invalid_payload = {
            'name': '',
            'description': None
        }

    def test_create_valid_contact(self):
        response = client.post(
            reverse('phonebook'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_contact(self):
        response = client.post(
            reverse('phonebook'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
