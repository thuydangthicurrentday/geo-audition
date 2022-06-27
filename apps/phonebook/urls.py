from django.urls import path
from rest_framework import routers

from apps.phonebook.views import PhonebookViewSet, EmailViewSet, PhoneNumberViewSet


router = routers.DefaultRouter()

router.register(r'phonebook', PhonebookViewSet, basename='phonebook-emails')
router.register(r'phonebook-emails', EmailViewSet, basename='phonebook-emails')
router.register(r'phonebook-phone-numbers', PhoneNumberViewSet, basename='phonebook-phone-numbers')

urlpatterns = router.urls
