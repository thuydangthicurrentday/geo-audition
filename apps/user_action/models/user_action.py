from django.db import models

# Create your models here.

class UserAction(models.Model):
    search_query = models.CharField(max_length=200)
    page_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(blank=True, max_length=1000)
