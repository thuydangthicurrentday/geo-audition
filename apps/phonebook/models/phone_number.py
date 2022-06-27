from django.db import models


class PhoneNumber(models.Model):
    phonebook = models.ForeignKey('phonebook.Phonebook', on_delete=models.CASCADE, related_name='phone_numbers')
    phone_number = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
