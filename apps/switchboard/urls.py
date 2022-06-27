from django.urls import path
from rest_framework import routers

from apps.switchboard.views import SwitchboardViewSet



router = routers.DefaultRouter()

router.register(r'switchboard', SwitchboardViewSet, basename='switchboard')

urlpatterns = router.urls + [
]
