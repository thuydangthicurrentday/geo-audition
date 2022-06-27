from rest_framework.viewsets import ModelViewSet
from apps.switchboard.models import Switchboard
from apps.switchboard.serializers import SwitchboardSerializer


class SwitchboardViewSet(ModelViewSet):
    """
    A viewset for viewing and editing Switchboard instances.
    """
    serializer_class = SwitchboardSerializer
    queryset = Switchboard.objects.all()
