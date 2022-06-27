from django.db import models


class Email(models.Model):
    phonebook = models.ForeignKey('phonebook.Phonebook', on_delete=models.CASCADE, related_name='emails')
    email = models.EmailField(max_length=100)
