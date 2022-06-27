from django.db import models


class Switchboard(models.Model):
    phone_number = models.CharField(max_length=30)
    description = models.CharField(max_length=1000, null=True, blank=True)
    is_active = models.BooleanField(default=True)
