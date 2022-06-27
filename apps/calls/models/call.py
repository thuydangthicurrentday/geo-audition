from django.db import models
from django.contrib.auth.models import User


class Call(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    note = models.CharField(max_length=200)
    consultant = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    switchboard_phone_number = models.ForeignKey('switchboard.Switchboard', on_delete=models.SET_NULL, null=True)
    user_phone_number = models.ForeignKey('phonebook.PhoneNumber', on_delete=models.SET_NULL, null=True)
