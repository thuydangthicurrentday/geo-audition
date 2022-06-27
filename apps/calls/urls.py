from django.urls import path
from rest_framework import routers
from apps.calls.views import CallViewSet


router = routers.DefaultRouter()

router.register(r'calls', CallViewSet, basename='calls')

urlpatterns = router.urls + [
]
